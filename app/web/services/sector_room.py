import requests
from services import rest_api

def sectors():
    answer = requests.get(f'{rest_api.API_URL}/sectors')
    return answer.json()

def sectorInfo(sectorId):
    answer = requests.get(f'{rest_api.API_URL}/sectors/{sectorId}')
    return answer.json()

def sectorUpdate(sectorId,name,photoURI,status,rooms):
    body={
        "name":name,
        "photoURI":photoURI,
        "status":status,
        "rooms":[rooms]
    }
    answer = requests.put(f'{rest_api.API_URL}/sectors/{sectorId}', json=body)
    return answer.status_code

def sectorNew(name,photoURI,rooms):
    body={
        "name":name,
        "photoURI":photoURI,
        "rooms":[rooms]
    }
    requests.post(f'{rest_api.API_URL}/sectors/new', json=body)
    body={
        "name":name
    }
    answer=requests.get(f'{rest_api.API_URL}/sectors/search', json=body)
    return answer.json()