from http.server import BaseHTTPRequestHandler
from pathlib import Path
from routes import routes


class Server(BaseHTTPRequestHandler):

    def do_HEAD(self):
        pass

    def do_POST(self):
        pass

    def do_GET(self):
        self.respond()

    def handle_http(self):
        status = 200
        content_type = "text/plain"
        response_content = ""

        if self.path in routes:
            route_content = routes[self.path]['template']
            filepath = Path(f"templates/{route_content}")
            if filepath.is_file():
                content_type = "text/html"
                response_content = open(f"templates/{route_content}")
                response_content = response_content.read()
            else:
                content_type = "text/plain"
                response_content = "404 Not Found"
        else:
            content_type = "text/plain"
            response_content = "404 Not Found"

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(response_content, "UTF-8")

    def respond(self):
        content = self.handle_http()
        self.wfile.write(content)
