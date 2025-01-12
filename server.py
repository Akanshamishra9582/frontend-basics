import http.server
import socketserver

# Define the port number to use
PORT = 8080

# Define the directory to serve files from
DIRECTORY = "FRONTEND-BASICS"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the base directory
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Set up the server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving files from {DIRECTORY} at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()
