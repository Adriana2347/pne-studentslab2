import http.client
import json
from Seq1 import Seq

server = "rest.ensembl.org"
endpoint = "/lookup/symbol/human/"
parameters = "?content-type=application/json"
URL = server + endpoint + parameters

endpoint_2 = "/sequence/id/"
parameters_2 = "?content-type=application/json"
URL_2 = server + endpoint + parameters

print(f"Server:{server}")
print(f"URL:{URL}")

conn = http.client.HTTPConnection(server)

genes_dict = {}
genes = ["FRAT1", "ADA", "FXN", "RNU6-269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
for gene in genes:
    print(gene)
    final_parameter = endpoint + gene + parameters
    conn.request("GET", final_parameter)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    if "id" in data:
        genes_dict[gene] = data["id"]

        new_parameter = endpoint_2 + genes_dict[gene] + parameters_2
        conn.request("GET", new_parameter)
        response = conn.getresponse()
        data_2 = json.loads(response.read().decode())

        if "seq" in data_2:
            d = data_2["seq"]
        if "desc" in data_2:
            print("Description:", data_2["desc"])

        s = Seq(data_2["seq"])
        print("Total lenght:", s.len())
        print("Total bases", s.count())
        count_dict = s.count()
        print("The most frequent base:", s.most_bases(count_dict))

print(genes_dict)

