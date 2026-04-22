import http.client
import json


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

final_parameter = endpoint + "MIR633" + parameters
conn.request("GET", final_parameter)
response = conn.getresponse()
data = json.loads(response.read().decode())
if "id" in data:
    id = data["id"]

    new_parameter = endpoint_2 + id + parameters_2
    conn.request("GET", new_parameter)
    response = conn.getresponse()
    data_2 = json.loads(response.read().decode())
    print("Gene: MIR633")
    if "seq" in data_2:
        print("Bases:", data_2["seq"])

    if "desc" in data_2:
        print("Description:", data_2["desc"])


