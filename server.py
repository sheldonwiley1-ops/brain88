import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/state":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps({
                "harmony": 88,
                "arc": 49,
                "state": "STABLE",
                "protocol": {
                    "breath_pattern": "4-4",
                    "sound_hz": 432,
                    "light_hex": "#7C3AED"
                }
            }).encode())

        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'ENGINE88 LIVE')

PORT = 8080
server = HTTPServer(('', PORT), handler)
print("Running on port", PORT)
server.serve_forever()
