import requests
import json

uri = 'http://127.0.0.1:8000/api/StudentAPI'

def Fetch_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=uri, data=json_data)
    print(r.json())


# Fetch_data('1')
    
def post_data():
    data = {
    'id':10,
    'first_name' : 'saloni',
    'last_name' : 'jagtap',
    'Roll_number' : 110
    }

    json_data = json.dumps(data)
    r = requests.post(url=uri,data=json_data)
    data2 = r.json()
    print(data2)

# post_data()
    
def update_data():
    data = {
    "id":12,
    "first_name" : "abcd@"
}

    json_data = json.dumps(data)
    r = requests.put(url=uri, data=json_data)
    data2 = r.json()
    print(data2)

update_data()
    
def delete_data():
    data = {'id':10}

    json_data = json.dumps(data)
    r = requests.delete(url = uri, data = json_data)

    data = r.json()

    print(data)

# delete_data()

