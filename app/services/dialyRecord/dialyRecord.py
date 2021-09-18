from data.models import dialyRecord as dialyRecord_Model

def create_dialyRecord(sectorId,roomId,auxNurseId, nurseId, createdDate, bed, pacientDocument, pacientName, pacientLastName, comment):
    dialyRecord_Model.create_dialyRecord(sectorId,roomId,auxNurseId, nurseId, createdDate, bed, pacientDocument, pacientName, pacientLastName, comment)

def view_dialyRecord(recordId):
    dialyRecord_Model.view_dialyRecord(recordId)

def view_dialyRecords():
    dialyRecord_Model.view_dialyRecords()
    
