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
        if "?" in url:
            final_url = url + "&content-type=application/json"
        else:
            final_url = url + "?content-type=application/json"
        conn.request("GET", final_url)
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

    def check_json(self, arguments):
        return arguments.get("json", ["0"])[0] == "1"

    def send_json(self, data, code=200):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        json_mode = self.check_json(arguments)

        body = "ninguna de las anteriores"

        file = path.strip("/")
        if file == "" or file == "index.html":
            filename = "html/index.html"
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            self.send_response(200)

        elif path == "/listSpecies":
            try:
                limit = arguments["limit"][0]
                if limit is None or limit == "":
                    new_limit = None
                else:
                    new_limit = int(limit)
                    url = "/info/species"
                    data = client_request(url)
                    species = json.loads(data)
                    species_list = []
                    for specie in species["species"]:
                        if "common_name" in specie:
                            species_list.append(specie["common_name"])
                        else:
                            species_list.append(specie["name"])
                        if new_limit is not None and len(species_list) >= new_limit:
                            break
                    species_list = ", ".join(species_list)

                    if json_mode:
                        return self.send_json({"Sequence": species_list, "Limit": new_limit})

                    body = self.read_html_file("list_species.html").render(context={"Sequence": species_list, "Limit": new_limit})
                    self.send_response(200)

            except Exception as error:
                body = self.read_html_file("error.html").render(
                    context={"error": str(error)})
                self.send_response(500)

        elif path == "/karyotype":
            try:
                specie = arguments["species"][0]
                url2 = "/info/assembly/" + specie
                data = client_request(url2)
                name_chromosomes = json.loads(data)
                if "karyotype" in  name_chromosomes:
                    chromosome_list = name_chromosomes["karyotype"]
                    chromosome_list = ", ".join(chromosome_list)
                    if json_mode:
                        return self.send_json({"Chromosome": chromosome_list})

                    body = self.read_html_file("chromosomes.html").render(context={"Chromosome": chromosome_list})
                    self.send_response(200)
                else:
                    body = self.read_html_file("error.html").render(context={"error": "Karyotype not found"})
                    self.send_response(400)
            except Exception as error:
                body = self.read_html_file("error.html").render(
                    context={"error": str(error)})
                self.send_response(500)

        elif path == "/chromosomeLength":
            try:
                specie = arguments["species"][0]
                chromo = arguments["chromo"][0]
                url2 = "/info/assembly/" + specie
                data = client_request(url2)
                name_chromosomes = json.loads(data)
                if "top_level_region" not in name_chromosomes:
                    body = self.read_html_file("error.html").render(context={"error": "Species not found"})
                    self.send_response(404)
                else:
                    length = None
                    for region in name_chromosomes["top_level_region"]:
                        if region["name"] == chromo:
                            length = region["length"]
                            break
                    if length is None:
                        body = self.read_html_file("error.html").render(
                            context={"error": "Chromosome not found"})
                        self.send_response(404)
                    else:
                        if json_mode:
                            return self.send_json({"length": length})

                        body = self.read_html_file("chromo_l.html").render(context={"length": length})
                        self.send_response(200)

            except Exception as error:
                body = self.read_html_file("error.html").render(
                    context={"error": str(error)})
                self.send_response(500)

        elif path == "/geneLookup":
            try:
                gene = arguments["gene"][0]
                url3 = "lookup/symbol/homo_sapiens/" + gene
                data = client_request(url3)
                gene_id = json.loads(data)
                if "id" in gene_id:
                    id_gene = gene_id["id"]
                    if json_mode:
                        return self.send_json({"id": id_gene, "gene":gene})
                    body = self.read_html_file("gene_id.html").render(context={"id": id_gene, "gene":gene})
                    self.send_response(200)
                else:
                    body = self.read_html_file("error.html").render(context={"error": "Species not found"})
                    self.send_response(400)

            except Exception as error:
                body = self.read_html_file("error.html").render(
                    context={"error": str(error)})
                self.send_response(500)

        elif path == "/geneSeq":
            try:
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
                        if json_mode:
                            return self.send_json({"sequence": sequence, "gene": gene})
                        body = self.read_html_file("geneSeq.html").render(context={"sequence": sequence, "gene": gene})
                        self.send_response(200)
                    else:
                        body = self.read_html_file("error.html").render(context={"error": "Species not found"})
                        self.send_response(400)

                else:
                    body = self.read_html_file("error.html").render(context={"error": "Species not found"})
                    self.send_response(400)


            except Exception as error:
                body = self.read_html_file("error.html").render(
                    context={"error": str(error)})
                self.send_response(500)

        elif path == "/geneInfo":
            try:
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
                        if json_mode:
                            return self.send_json({"end": end, "start": start, "chromosome": chromosome, "length": length})
                        body = self.read_html_file("gene_info.html").render(context={"end": end, "start": start, "chromosome": chromosome, "length": length})
                        self.send_response(200)
                else:
                    body = self.read_html_file("error.html").render(context={"error": "Species not found"})
                    self.send_response(400)
            except Exception as error:
                body = self.read_html_file("error.html").render(
                    context={"error": str(error)})
                self.send_response(500)

        elif path == "/geneCalc":
            try:
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
                        if json_mode:
                            return self.send_json({"length": total_len, "bases": total_bases, "percentage": porcentage})
                        body = self.read_html_file("gene_calc.html").render(context={"length": total_len, "bases": total_bases, "percentage": porcentage})
                        self.send_response(200)
                else:
                    body = self.read_html_file("error.html").render(context={"error": "Species not found"})
                    self.send_response(400)
            except Exception as error:
                body = self.read_html_file("error.html").render(
                    context={"error": str(error)})
                self.send_response(500)

        elif path == "/geneList":
            try:
                start = arguments["start"][0]
                end = arguments["end"][0]
                chromo = arguments["chromo"][0]
                result_list = []
                url6 = f"/overlap/region/human/{chromo}:{start}-{end}?feature=gene"
                data = client_request(url6)
                gene_identified = json.loads(data)
                if not gene_identified:
                    body = self.read_html_file("error.html").render(context={"error": "Species not found"})
                    self.send_response(400)
                else:
                    for gen in gene_identified:
                        if "external_name" in gen:
                            gene_name = gen["external_name"]
                            result_list.append(gene_name)
                        result_list = ", ".join(result_list)
                        if json_mode:
                            return self.send_json({"result_list": result_list})
                        body = self.read_html_file("gene_list.html").render(context={"result_list": result_list})
                        self.send_response(200)
            except Exception as error:
                body = self.read_html_file("error.html").render(
                    context={"error": str(error)})
                self.send_response(500)

        else:
            body = self.read_html_file("error.html").render(context={"error": "Species not found"})
            self.send_response(400)

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