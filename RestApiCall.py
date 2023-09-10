import http.client

conn = http.client.HTTPSConnection("api.xyz.com")
payload = ''
headers = {}
conn.request("GET", "/?name=anupam", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
