import requests
import json

url = 'http://127.0.0.1:8000/api/Delete'

data = {'id':10}

json_data = json.dumps(data)
r = requests.delete(url = url, data = json_data)

data = r.json()

print(data)