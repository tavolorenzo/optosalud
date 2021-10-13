import requests
from web.services import rest_api

def valid_credentials(documment,password):
    body = {
        "documment": documment,
        "password":password
    }
    answer = requests.post(f'{rest_api.API_URL}/login', json=body)
    return answer.status_code == 200