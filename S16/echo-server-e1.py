import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# Define the Server's port
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True



class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):


        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)

        contents = Path('html/form-e1.html').read_text()

        file = self.path.strip("/")
        if file == "" or file == "index.html":
            filename = "html/form-e1.html"
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            self.send_response(200)
        elif path == "/echo":
            message = arguments.get("message", [""])[0]
            body = f"""
                        <html>
                            <body>
                                <p>{message}</p>
                                <a href="/">Main page</a>
                            </body>
                        </html>
                        """
            self.send_response(200)
        else:
            filename = "html/error.html"
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            self.send_response(404)



        termcolor.cprint(self.requestline, 'green')


        contents = Path('html/form-e1.html').read_text()

        # Generating the response message
         # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body.encode("utf-8"))))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(body.encode("utf-8"))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
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
