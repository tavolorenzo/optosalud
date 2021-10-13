from data.models import dialyRecord as dialyRecord_Model

def create_dialyRecord(sectorId,roomId,auxNurseId, nurseId, bed, pacientDocument, pacientName, pacientLastName, comment): #OK
    dialyRecord_Model.create_dialyRecord(sectorId,roomId,auxNurseId, nurseId, bed, pacientDocument, pacientName, pacientLastName, comment)

def view_dialyRecord(recordId): #OK
    return dialyRecord_Model.view_dialyRecord(recordId)

def view_dialyRecords(): #OK
    return dialyRecord_Model.view_dialyRecords()
    
