import requests
from services import rest_api



def users_by_JobPosition(jobPosition):
    body = {
        "jobPosition":jobPosition,
    }
    answer = requests.get(f'{rest_api.API_URL}/users/search',json=body)
    return answer.json()

def userInfo(userId):
    answer = requests.get(f'{rest_api.API_URL}/users/{userId}')
    return answer.json()