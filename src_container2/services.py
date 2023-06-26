import requests
import json


def get_notes():
    response = requests.get('http://container1:5000/notes')
    temp = response.content.decode('utf8').replace("'", '"')
    data = json.loads(temp)
    return data['notes']
