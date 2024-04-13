import requests
import json

URL = 'http://127.0.0.1:8000/api/Update'

data = {
    "id": 10,
    "first_name": "ABC",
    "last_name": "XYZ",
}

json_data = json.dumps(data)
r = requests.put(url=URL, data=json_data)
data2 = r.json()
print(data2)