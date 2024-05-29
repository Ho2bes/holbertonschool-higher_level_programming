#!/usr/bin/python3
"""A Simple API using Python's http.server module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='text/plain'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self._set_headers(content_type='application/json')
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write(b'OK')
        else:
            self._set_headers(status_code=404)
            self.wfile.write(b'Endpoint not found')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()
