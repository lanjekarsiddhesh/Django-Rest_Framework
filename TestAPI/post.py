import requests
import json

URL = 'http://127.0.0.1:8000/api/Store'

data = {
    'id':10,
    'first_name' : 'saloni',
    'last_name' : 'jagtap',
    'Roll_number' : 110
}

json_data = json.dumps(data)
r = requests.post(url=URL,data=json_data)
data2 = r.json()
print(data2)