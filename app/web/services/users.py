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

def updateUser(userId,phone, email, photoURI, jobPosition, password, roleId, status):
    body={
        "phone":phone,
        "email":email,
        "photoURI":photoURI,
        "jobPosition":jobPosition,
        "password":password,
        "roleId":roleId,
        "status":status
    }
    answer=requests.put(f'{rest_api.API_URL}/users/{userId}',json=body)
    return answer.status_code

def getUserId(document):
    body = {
        "document":document,
    }
    userId = requests.get(f'{rest_api.API_URL}/users' , json = body)
    answer = requests.get(f'{rest_api.API_URL}/users/{userId.json()[0]["userId"]}')
    return answer.json()
 