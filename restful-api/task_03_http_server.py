#!/usr/bin/python3
"""Simple HTTP API built with Python's http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle simple GET endpoints for the API."""

    def do_GET(self):
        """Serve text, JSON, or a 404 response for known endpoints."""
        path = urlparse(self.path).path

        if path == "/":
            self._send_text(200, "Hello, this is a simple API!")
            return

        if path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
            return

        if path == "/status":
            self._send_text(200, "OK")
            return

        if path == "/info":
            self._send_json(
                200,
                {"version": "1.0", "description": "A simple API built with http.server"},
            )
            return

        self._send_json(404, {"error": "Endpoint not found"})

    def _send_text(self, status_code, message):
        """Send a plain text response."""
        body = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status_code, payload):
        """Send a JSON response."""
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        """Suppress default logging noise for cleaner output."""
        return


def main():
    """Run the simple API server on port 8000."""
    server = HTTPServer(("0.0.0.0", 8000), SimpleAPIHandler)
    print("Server running on http://localhost:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
