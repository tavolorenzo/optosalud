import requests
from services import rest_api

def sectors():
    answer = requests.get(f'{rest_api.API_URL}/sectors')
    return answer.json()

def rooms(sectorId):
    answer = requests.get(f'{rest_api.API_URL}/sectors/{sectorId}')
    return answer.json()


