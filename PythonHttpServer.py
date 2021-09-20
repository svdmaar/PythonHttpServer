import http.server
import socketserver

port = 8080

class MyHttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
            super().do_GET()
        else:
            super().do_GET()

with socketserver.TCPServer(("", port), MyHttpHandler) as httpd:
    httpd.serve_forever()

