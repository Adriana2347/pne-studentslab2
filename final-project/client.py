import http.client
import json

server = "localhost"
PORT = 8080

def request_server(path):
    conn = http.client.HTTPConnection(server, PORT)
    conn.request("GET", path)
    response = conn.getresponse()
    return json.loads(response.read().decode())

print("---ListSpecies---")
data = request_server("/listSpecies?limit=10&json=1")
print(data)

print("---karyotype---")
data = request_server("/karyotype?species=mouse&json=1")
print(data)

print("---chromosomeLength---")
data = request_server("/chromosomeLength?species=mouse&chromo=18&json=1")
print(data)

print("---geneLookup---")
data = request_server("/geneLookup?gene=FRAT1&json=1")
print(data)

print("---geneSeq---")
data = request_server("/geneSeq?gene=FRAT1&json=1")
print(data)

print("---geneInfo---")
data = request_server("/geneInfo?gene=FRAT1&json=1")
print(data)

print("---geneCalc---")
data = request_server("/geneCalc?gene=FRAT1&json=1")
print(data)

print("---geneList---")
data = request_server("/geneList?chromo=9&start=22125500&end=22136000&json=1")
print(data)