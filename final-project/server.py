import http.server
import socketserver
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import termcolor
from pathlib import Path
import http.client


PORT = 8080

socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def read_html_file(self, filename):
        contents = Path("html/" + filename).read_text(encoding="utf-8")
        content = j.Template(contents)
        return content

    def do_GET(self):

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        print(path)

        file = path.strip("/")
        if file == "" or file == "index.html":
            filename = "html/index.html"
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            self.send_response(200)

        elif path == "/listSpecies":
            limit = arguments["limit"][0]
            i = 0
            species_list = {}
            while i < limit:
                for specie in species:
                    if "common_name" in specie:
                        i += 1
                        species_list += specie["common_name"]
                        body = self.read_html_file("html/list_species.html").render(context={"Text": "The server is alive!"})
            self.send_response(200)
        termcolor.cprint(self.requestline, 'green')

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body.encode("utf-8"))))

            # The header is finished
        self.end_headers()

            # Send the response message
        self.wfile.write(body.encode("utf-8"))

        return

Handler = TestHandler

    # -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

        # -- Main loop: Attend the client. Whenever there is a new
        # -- clint, the handler is called
    try:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()