import requests
from services import rest_api

def valid_credentials(document,password):
    body = {
        "document":document,
        "password":password
    }
    answer = requests.post(f'{rest_api.API_URL}/login', json=body)
    return answer.status_code == 200

def session_info(document):
    body = {
        "document":document,
    }
    userId = requests.get(f'{rest_api.API_URL}/users' , json = body)
    answer = requests.get(f'{rest_api.API_URL}/users/{userId.json()[0]["userId"]}')
    return answer.json()
