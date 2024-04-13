import requests
import json

uri = 'http://127.0.0.1:8000/api/GetStudentData'

# r = requests.get(url = uri)

# data = r.json()

# print(data)

def Fetch_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=uri, data=json_data)
    print(r.json())


Fetch_data()