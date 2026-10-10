"""Local-only web dashboard and CLI for CareContinuity Lab."""
from __future__ import annotations

import argparse
import json
import os
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from .engine import assess, assess_file, load_scenario, sha256_file, validate_services

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TIMELINE_PATH = DATA / "ummc_public_timeline.json"
DEFAULT_SCENARIO = DATA / "training_scenario.json"
REPORTS = ROOT / "reports"


def assessment_html(result: dict) -> str:
    workflows = "".join(
        f"<article class='workflow'><div><span class='pill {item['status'].replace(' ', '-')}'>{item['status'].upper()}</span><b>{item['workflow']}</b></div><p>Exercise impact: {item['impact_score']} / 5 · Affected: {', '.join(item['affected_services']) or 'none'}</p><ul>{''.join(f'<li>{action}</li>' for action in item['continuity_actions'])}</ul></article>"
        for item in result["workflows"]
    )
    services = "".join(
        f"<span class='service {s['state']}'><b>{s['service']}</b><small>{s['state']}</small></span>"
        for s in result["services"]
    )
    return f"<section class='result'><div class='score'><div><small>TABLETOP IMPACT</small><strong>{result['aggregate_exercise_score']}<i> / {result['aggregate_maximum']}</i></strong></div><p>Operational exercise indicator<br>Not a patient risk or clinical score</p></div><div class='servicegrid'>{services}</div><h3>Workflow impact and continuity prompts</h3>{workflows}<button id='save'>Save exercise record</button><pre id='saved'></pre></section>"


class Handler(BaseHTTPRequestHandler):
    server_version = "CareContinuityLab/1.0"

    def _send(self, status: int, body: bytes, content_type: str = "text/html; charset=utf-8") -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path != "/":
            self._send(404, b"Not found", "text/plain; charset=utf-8")
            return
        template = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
        timeline = json.loads(TIMELINE_PATH.read_text(encoding="utf-8"))
        facts = "".join(
            f"<article class='timelineitem'><time>{event['date']}</time><b>{event['label']}</b><p>{event['detail']}</p><a href='{event['source_url']}' target='_blank' rel='noopener'>{event['source_name']} ↗</a><small>{event['evidence_type']}</small></article>"
            for event in timeline["events"]
        )
        unresolved = "".join(f"<li>{fact}</li>" for fact in timeline["unresolved_public_facts"])
        html = template.replace("{{TIMELINE}}", facts).replace("{{UNRESOLVED}}", unresolved)
        self._send(200, html.encode("utf-8"))

    def do_POST(self) -> None:
        route = urlparse(self.path).path
        if route not in {"/api/assess", "/api/save"}:
            self._send(404, b'{"error":"not found"}', "application/json")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 1 or length > 10_000:
                raise ValueError("request body must be between 1 and 10000 bytes")
            request = json.loads(self.rfile.read(length))
            if route == "/api/save":
                if not isinstance(request, dict) or request.get("tool") != "CareContinuity Lab":
                    raise ValueError("only a CareContinuity Lab assessment can be saved")
                REPORTS.mkdir(parents=True, exist_ok=True)
                output = REPORTS / "browser-tabletop-assessment.json"
                serialized = json.dumps(request, indent=2) + "\n"
                output.write_text(serialized, encoding="utf-8")
                import hashlib
                response = {"path": str(output.relative_to(ROOT)), "sha256": hashlib.sha256(serialized.encode("utf-8")).hexdigest()}
                self._send(200, json.dumps(response).encode("utf-8"), "application/json; charset=utf-8")
                return
            values = request.get("services", {})
            validate_services(values)
            result = assess({
                "scenario_name": "Browser tabletop scenario",
                "scenario_type": "synthetic user-created exercise",
                "services": values,
                "exercise_note": "This is a training exercise, not UMMC internal data. Confirm local clinical downtime procedures with authorized leaders."
            })
            body = json.dumps(result).encode("utf-8")
            self._send(200, body, "application/json; charset=utf-8")
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            self._send(400, json.dumps({"error": str(exc)}).encode("utf-8"), "application/json; charset=utf-8")

    def log_message(self, fmt: str, *args) -> None:
        print("[CareContinuity] " + fmt % args)


def main() -> int:
    parser = argparse.ArgumentParser(description="Healthcare downtime tabletop and UMMC public case viewer")
    subparsers = parser.add_subparsers(dest="command")
    assess_parser = subparsers.add_parser("assess", help="assess a local tabletop scenario JSON file")
    assess_parser.add_argument("scenario", nargs="?", type=Path, default=DEFAULT_SCENARIO)
    assess_parser.add_argument("--output", type=Path, default=REPORTS / "demo-assessment.json")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8765")), help="dashboard port (default: 8765, or the hosting provider's PORT)")
    parser.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"), help="network interface (default: 127.0.0.1 for local use)")
    parser.add_argument("--open", action="store_true", help="open the local dashboard in a browser")
    args = parser.parse_args()
    if args.command == "assess":
        try:
            result = assess_file(args.scenario)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            parser.error(str(exc))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(f"Workflows reviewed: {len(result['workflows'])}")
        print(f"Exercise impact score: {result['aggregate_exercise_score']} / {result['aggregate_maximum']}")
        print(f"Scenario SHA-256: {result['scenario_sha256']}")
        print(f"Record: {args.output}")
        return 0
    if not 1024 <= args.port <= 65535:
        parser.error("port must be between 1024 and 65535")
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    url = f"http://{args.host}:{args.port}"
    print(f"CareContinuity Lab is running at {url}. Press Ctrl+C to stop.")
    if args.open:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping CareContinuity Lab.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
