import http.server
import socketserver
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import termcolor
from pathlib import Path
import http.client
import json


PORT = 8080


def client_request(url):
    conn = http.client.HTTPSConnection("rest.ensembl.org")
    conn.request("GET", url+"?content-type=application/json")
    response = conn.getresponse()
    data = response.read().decode("utf-8")

    conn.close()
    return data

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
        print(arguments)

        file = path.strip("/")
        if file == "" or file == "index.html":
            filename = "html/index.html"
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            self.send_response(200)

        elif path == "/listSpecies":
            limit = arguments["limit"][0]
            if limit is None or limit == "":
                new_limit = None
            else:
                new_limit = int(limit)

            url = "/info/species"
            data = client_request(url)
            species = json.loads(data)
            species_list = []
            name = species.get("common_name") or species.get("name")
            for specie in species:
                if name in specie:
                    species_list.append(specie[name])
                    if new_limit is not None and len(species_list) >= new_limit:
                        break

            body = self.read_html_file("list_species.html").render(context={"Sequence": species_list,"Limit": new_limit})
            self.send_response(200)

        elif path == "/karyotype":
            specie = str(arguments["limit"][0])
            url2 = "/info/assembly/" + specie
            data = client_request(url2)
            name_chromosomes = json.loads(data)
            chromosome_list = []
            if "name" in name_chromosomes:
                chromosome_list.append(name_chromosomes["name"])
            body = self.read_html_file("chromosomes.html").render(context={"Chromosome": chromosome_list})
            self.send_response(200)


        else:
            self.send_response(404)
            body = "404 Not Found"

        termcolor.cprint(self.requestline, 'green')
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

        return

Handler = TestHandler

    # -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()