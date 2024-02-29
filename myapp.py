import requests
import json

# URL = "http://127.0.0.1:8000/stuinfo/"
# r = requests.get(url=URL)
# data = r.json()
# print(data)

URL = "http://127.0.0.1:8000/studentapp/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    # print("===============>", json_data)
    r = requests.get(url=URL, data=json_data)
    try:
        data = r.json()
    except:
        print("Data Not Found")
    print(data)
# get_data()


def post_data():
    data = {
        "name": "foram",
        "roll": 25,
        "city": "deesa",
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
post_data()


def update_data():
    data = {
        "id": 18,
        "name": "krish",
        "city": "hirpura"
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
#update_data()

def delete_data():
    data = {
        "id": 15
    }

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
#delete_data()
