import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = os.path.abspath('.')  # This gets the absolute path to the current directory

print(f"Current working directory: {DIRECTORY}")  # Prints the directory path

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving files from {DIRECTORY} at http://localhost:{PORT}")
    httpd.serve_forever()
