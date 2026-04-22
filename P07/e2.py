import http.client
import json


server = "rest.ensembl.org"
endpoint = "/lookup/symbol/human/"
parameters = "?content-type=application/json"
URL = server + endpoint + parameters

print(f"Server:{server}")
print(f"URL:{URL}")

conn = http.client.HTTPConnection(server)

genes_dict = {}
genes = ["FRAT1", "ADA", "FXN", "RNU6-269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
for gene in genes:
    final_parameter = endpoint + gene + parameters
    conn.request("GET", final_parameter)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    if "id" in data:
        genes_dict[gene] = data["id"]
print(genes_dict)




