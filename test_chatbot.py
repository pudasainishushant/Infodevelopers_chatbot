import requests
import json

endpoint = "http://localhost:5005/webhooks/rest/webhook"

json_body = {
    "sender":"rasa",
    "message":"vacation"
}

headers = {
    "Content-type":"application/json"
}

result = requests.post(url=endpoint,data=json.dumps(json_body),headers=headers)

print(result.status_code)
print(result.content)
