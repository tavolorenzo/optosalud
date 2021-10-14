import requests
from services import rest_api

def valid_credentials(document,password):
    body = {
        "document":document,
        "password":password
    }
    answer = requests.post(f'{rest_api.API_URL}/login', json=body)
    return answer.status_code == 200