import json
import datetime

data = {
    "id": 123,
    "name": "Anupam Kumar Dwivedi",
    "saley": 11000,
    "updated": datetime.datetime.now()
}

def default(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()

print("JSON Data")
print(json.dumps(data, default=default))
