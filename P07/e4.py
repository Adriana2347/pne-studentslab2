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

gene = input("Enter a valid gene: ")
final_parameter = endpoint + gene + parameters
conn.request("GET", final_parameter)
response = conn.getresponse()
data = json.loads(response.read().decode())
if "id" in data:
    id = data["id"]


    new_parameter = endpoint_2 + id + parameters_2
    conn.request("GET", new_parameter)
    response = conn.getresponse()
    data_2 = json.loads(response.read().decode())
    print(gene)
    if "seq" in data_2:
        print("Bases:", data_2["seq"])
    if "desc" in data_2:
        print("Description:", data_2["desc"])

    s = Seq(data_2["seq"])
    print("Total lenght:", s.len())
    print("Total bases", s.count())
    count_dict = s.count()
    print("The most frequen base:", s.most_bases(count_dict))

