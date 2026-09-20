import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = int(os.environ.get("PORT", 8080))

with TCPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler) as server:
    print(f"Server running on port {PORT}")
    server.serve_forever()