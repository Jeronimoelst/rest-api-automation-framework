import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_request(endpoint):
    url = BASE_URL + endpoint
    response = requests.get(url)

    return response 

def post_request(endpoint, payload):
    url = BASE_URL + endpoint
    response = requests.post(url, json=payload)
    return response