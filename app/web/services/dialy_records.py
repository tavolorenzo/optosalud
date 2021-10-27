import requests
from services import rest_api


def newDialyRecord(sectorId, roomId, auxNurseId, nurseId, bed, pacientDocument, pacientName, pacientLastName, comment):
    body = {
        "sectorId":sectorId,
        "roomId":roomId, 
        "auxNurseId":auxNurseId, 
        "nurseId":nurseId, 
        "bed":bed, 
        "pacientDocument":pacientDocument,
        "pacientName":pacientName, 
        "pacientLastName":pacientLastName, 
        "comment":comment
    }
    answer = requests.post(f'{rest_api.API_URL}/dialy_records/new',json=body)
    return answer.status_code == 200

def dialyrecords():
    answer = requests.get(f'{rest_api.API_URL}/dialy_records')
    return answer.json()

def dialyrecord(recordId):
    answer = requests.get(f'{rest_api.API_URL}/dialy_records/{recordId}')
    return answer.json()