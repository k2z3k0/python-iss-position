import requests
import json

response = requests.get('http://api.open-notify.org/iss-now.json')

count = 0
while (count < 3):
    query = {}
    response = requests.get('http://api.open-notify.org/astros.json', params=query)
    print(response.json())

