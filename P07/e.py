import http.client
import json


server = "rest.ensembl.org"
endpoint = "/info/ping"
parameters = "?content-type=application/json"
URL = server + endpoint + parameters

print(f"Server:{server}")
print(f"URL:{URL}")

conn = http.client.HTTPConnection(server)
conn.request("GET", endpoint + parameters)

response = conn.getresponse()
data = json.loads(response.read().decode())

if data["ping"] == 1:
    print("ALIVE!")
else:
    print("ERROR!")