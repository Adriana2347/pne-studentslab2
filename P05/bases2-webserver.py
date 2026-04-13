import http.server
import socketserver


PORT = 8080


socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        file = self.path.strip("/")
        if file == "/" or file == "/index.html":
            filename = "html/index.html"
        else:
            filename = "html/" + file
        try:
                with open(filename, "r", encoding="utf-8") as f:
                    body = f.read()
                    self.send_response(200)

        except:
            with open("html/error.html", "r", encoding="utf-8") as f:
                body = f.read()
                self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body.encode())
        return


Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()