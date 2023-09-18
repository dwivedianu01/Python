import http.client
import json

conn = http.client.HTTPSConnection("api-test.dhl.com", )
payload = json.dumps({
  "approverId": "user1",
  "extRequestRef": "RITM4403921",
  "requesterId": "anupam",
  "subscriberId": "12063010"
})
headers = {
  'Authorization': 'Bearer <id>',
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/service/tool/jira/1/user/subscribe", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
