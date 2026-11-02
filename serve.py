#!/usr/bin/env python3
"""
IntelliLearn Local Server
CS3613 Introduction to Artificial Intelligence Study Platform
"""

import http.server
import socketserver
import os
import webbrowser
import sys

PORT = 3613

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for local development & module script loading
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

    def guess_type(self, path):
        # Ensure .md and font mime types are served correctly
        if path.endswith('.md'):
            return 'text/markdown; charset=utf-8'
        elif path.endswith('.woff2'):
            return 'font/woff2'
        elif path.endswith('.woff'):
            return 'font/woff'
        elif path.endswith('.ttf'):
            return 'font/ttf'
        elif path.endswith('.js'):
            return 'application/javascript; charset=utf-8'
        return super().guess_type(path)

def main():
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    port = PORT
    handler = CustomHTTPRequestHandler
    
    # Attempt to bind, fall back to next open port if 3613 is in use
    httpd = None
    for p in range(port, port + 20):
        try:
            httpd = socketserver.TCPServer(("", p), handler)
            port = p
            break
        except OSError:
            continue

    if not httpd:
        print("Error: Could not bind to any port between 3613 and 3633.")
        sys.exit(1)

    url = f"http://localhost:{port}/"
    print("=" * 60)
    print(f"[IntelliLearn] CS3613 AI Study Platform")
    print(f"Serving locally from: {web_dir}")
    print(f"Open URL: {url}")
    print("Press Ctrl+C to stop the server.")
    print("=" * 60)

    try:
        webbrowser.open(url)
    except Exception:
        pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == "__main__":
    main()
