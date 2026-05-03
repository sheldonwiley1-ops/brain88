from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(b'ENGINE88 LIVE')

PORT = 8080
server = HTTPServer(('', PORT), handler)
print("Running on port", PORT)
server.serve_forever()
