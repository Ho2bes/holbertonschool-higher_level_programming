#!/usr/bin/python3
"""A Simple API using Python's http.server module"""

import http.server
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        endpoints = {
            "/data": {"name": "John", "age": 30, "city": "New York"},
            "/status": {"status": "OK"},
            "/info": {"vers": "1.0", "descript": "A simple API using http.server"}
        }

        if self.path in endpoints:
            data = endpoints[self.path]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())


PORT = 8000

with http.server.HTTPServer(("", PORT), MyHandler) as httpd:
    print(f"Server active on port {PORT}")
    httpd.serve_forever()
