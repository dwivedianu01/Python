import http.client
import json

conn = http.client.HTTPSConnection("devtools-test.dhl.com", )
payload = json.dumps({
  "approverId": "dpfeffer",
  "extRequestRef": "RITM4403921",
  "requesterId": "anupamdw",
  "subscriberId": "12063010"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwibGRhcCI6IkFOVVBBTURXIiwiZW1haWwiOiJhbnVwYW0uZHdpdmVkaUBkaGwuY29tIiwiYXV0aE1ldGhvZCI6IlRPS0VOIiwiaWF0IjoxNjc1MzE1OTIxLCJleHAiOjIwMzMxMTQ3MjF9.2iloiJ5g30FY5UgsNcrl5i_CO2Y-JEybqLaCcsE9GeA',
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/service/tool/jira/1/user/subscribe", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
