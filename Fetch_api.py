import requests

uri = 'http://127.0.0.1:8000/api/GetStudentData'

r = requests.get(url = uri)

data = r.json()

print(data)