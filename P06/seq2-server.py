import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from Seq1 import Seq

import jinja2 as j


# Define the Server's port
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

import jinja2 as j




class TestHandler(http.server.BaseHTTPRequestHandler):

    sequences = {0: "ACGTGACGAACGTA",
                 1: "TGCCCCCAGTTACC",
                 2: "CGTTAGTACCCATG",
                 3: "ACGGGTCGATGCAA",
                 4: "AAAGTGGTACCCAA"}


    def read_html_file(self, filename):
        contents = Path("html/" + filename).read_text(encoding="utf-8")
        content = j.Template(contents)
        return content

    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        print(arguments)

        file = self.path.strip("/")
        if file == "" or file == "index.html":
            filename = "html/index.html"
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            self.send_response(200)

        elif path == "/ping":
            body = self.read_html_file("ping.html").render(context={"Text": "The server is alive!"})
            self.send_response(200)

        elif path == "/get":
            data = int(arguments["n"][0])
            if data in self.sequences:
                body = self.read_html_file("get.html").render(context={"Sequence": self.sequences[data], "data": data})
                self.send_response(200)

        elif path == "/gene":
            name = arguments["name"][0]
            filename = "sequences/" + name + ".txt"
            s = Seq()
            s.read_fasta(filename)
            body = self.read_html_file("gene.html").render(context={"Sequence": str(s)})
            self.send_response(200)


        else:
            filename = "html/error.html"
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            self.send_response(404)

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