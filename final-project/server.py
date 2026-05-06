import http.server
import socketserver
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import termcolor
from pathlib import Path
import http.client
import json
from Seq1 import Seq


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

        body = "ninguna de las anteriores"

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
            specie = arguments["species"][0]
            url2 = "/info/assembly/" + specie
            data = client_request(url2)
            name_chromosomes = json.loads(data)
            chromosome_list = []
            if "karyotype" in name_chromosomes:
                chromosome_list.append(name_chromosomes["karyotype"])
            body = self.read_html_file("chromosomes.html").render(context={"Chromosome": chromosome_list})
            self.send_response(200)

        elif path == "/chromosomeLength":
            specie = arguments["species"][0]
            chromo = arguments["chromo"][0]
            url2 = "/info/assembly/" + specie
            data = client_request(url2)
            name_chromosomes = json.loads(data)
            length = []
            if "top_level_region" in name_chromosomes:
                for region in name_chromosomes["top_level_region"]:
                    if region["name"] == chromo:
                        length.append(region["length"])
            if not length:
                length = "Chromosome not found"

            body = self.read_html_file("chromo_l.html").render(context={"length": length})
            self.send_response(200)

        elif path == "/geneLookup":
            gene = arguments["gene"][0]
            url3 = "lookup/symbol/homo_sapiens/" + gene
            data = client_request(url3)
            gene_id = json.loads(data)
            if "id" in gene_id:
                id_gene = gene_id["id"]
                body = self.read_html_file("gene_id.html").render(context={"id": id_gene, "gene":gene})
                self.send_response(200)
            else:
                self.send_response(404)
                body = "404 Not Found"

        elif path == "/geneSeq":
            gene = arguments["gene"][0]
            url3 = "lookup/symbol/homo_sapiens/" + gene
            data = client_request(url3)
            gene_id = json.loads(data)
            if "id" in gene_id:
                id_gene = gene_id["id"]
                url4 = "sequence/id/" + id_gene
                data2 = client_request(url4)
                seq = json.loads(data2)
                if "seq" in seq:
                    sequence = seq["seq"]
                    body = self.read_html_file("geneSeq.html").render(context={"sequence": sequence, "gene": gene})
                    self.send_response(200)
                else:
                    self.send_response(404)
                    body = "404 Not Found"
            else:
                self.send_response(404)
                body = "404 Not Found"

        elif path == "/geneInfo":
            gene = arguments["gene"][0]
            url3 = "lookup/symbol/homo_sapiens/" + gene
            data = client_request(url3)
            gene_id = json.loads(data)
            if "id" in gene_id:
                id_gene = gene_id["id"]
                url5 = "lookup/id/" + id_gene
                data = client_request(url5)
                gene_info = json.loads(data)
                if "start" in gene_info:
                    start = gene_info["start"]
                if "end" in gene_info:
                    end = gene_info["end"]
                if "seq_region_name" in gene_info:
                    chromosome = gene_info["seq_region_name"]
                if start is not None and end is not None:
                    length = end - start
            body = self.read_html_file("gene_info.html").render(context={"end": end, "start": start, "chromosome": chromosome, "length": length})
            self.send_response(200)

        elif path == "/geneCalc":
            gene = arguments["gene"][0]
            url3 = "lookup/symbol/homo_sapiens/" + gene
            data = client_request(url3)
            gene_id = json.loads(data)
            if "id" in gene_id:
                id_gene = gene_id["id"]
                url4 = "sequence/id/" + id_gene
                data2 = client_request(url4)
                seq = json.loads(data2)
                if "seq" in seq:
                    sequence = seq["seq"]
                    s = Seq(sequence)
                    total_bases = s.count()
                    total_len = s.len()
                    porcentage = {}
                    for base, quantity in total_bases.items():
                        porcentage[base] = round((quantity / total_len) * 100, 2)
                    body = self.read_html_file("gene_calc.html").render(context={"length": total_len, "bases": total_bases, "percentage": porcentage})
                    self.send_response(200)
        elif path == "/geneList":
            start = arguments["start"][0]
            end = arguments["end"][0]
            chromo = arguments["chromo"][0]

            result_list = []



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