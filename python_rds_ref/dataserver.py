import sys
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

def start_server(PORT=8080):
    Handler = http.server.SimpleHTTPRequestHandler
    Handler.extensions_map={
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.jpeg': 'image/jpg',
        '.webp': 'image/webp',
        '.svg': 'image/svg+xml',
        '.css': 'text/css',
        '.txt': 'text/plain',
        '.js' : 'text/javascript',
        '.json': 'application/json',
        '': 'application/octet-stream', # Default
    }
    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("serving at port", PORT)
    httpd.serve_forever()

def cli(args=None):
    import argparse
    parser = argparse.ArgumentParser(description="Start a http mime fileserver")
    parser.add_argument("--port", default=8080, type=int)

    args = parser.parse_args(args)
    start_server(args.port)
