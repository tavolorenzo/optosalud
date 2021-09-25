from data.databases.connectDB import database 

def create_dialyRecord(sectorId,roomId,auxNurseId, nurseId, bed, pacientDocument, pacientName, pacientLastName, comment):
    sql_sentence = f"""
        INSERT INTO dialyRecord(sectorId,roomId,auxNurseId, nurseId,  bed, pacientDocument, pacientName, pacientLastName, comment)
        VALUES ('{sectorId}','{roomId}','{auxNurseId}', '{nurseId}', '{bed}', '{pacientDocument}', '{pacientName}', '{pacientLastName}', '{comment}')
    """
    bd=database()
    bd.run_sql(sql_sentence)

def view_dialyRecord(recordId):
    sql_sentence = f"""
    SELECT dialyRecord.*, sector.name AS SectorName, room.name AS RoomName, 
    user.name AS NurseName, user.lastName AS NurseLastName
    FROM dialyRecord
    INNER JOIN sector ON dialyRecord.sectorId=sector.sectorId
    INNER JOIN room ON dialyRecord.roomId=room.roomId
    INNER JOIN user ON dialyRecord.nurseId=user.userId 
    WHERE recordId='{recordId}'
    """
#    INNER JOIN user ON dialyRecord.auxNurseId=user.userId ambigus colum name
    bd=database()
    return [{"recordId": entry[0],
             "createdDate": entry[1],
             "bed": entry[2],
             "pacientDocument": entry[3],
             "pacientLastName": entry[4],
             "comment": entry[5],
             "nurseId": entry[6],
             "auxNurseId": entry[7],
             "sectorId": entry[8],
             "roomId": entry[9],
             "SectorName": entry[10],
             "roomName": entry[11],
             "nurseName": entry[12],
             "nurseLastName": entry[13]
             } for entry in bd.run_sql(sql_sentence)]

def view_dialyRecords():
    sql_sentence = f"""
    SELECT dialyRecord.*, sector.name AS SectorName, room.name AS RoomName, 
    user.name AS NurseName, user.lastName AS NurseLastName
    FROM dialyRecord 
    INNER JOIN sector ON dialyRecord.sectorId=sector.sectorId
    INNER JOIN room ON dialyRecord.roomId=room.roomId
    INNER JOIN user ON dialyRecord.nurseId=user.userId
    """
#    INNER JOIN user ON dialyRecord.auxNurseId=user.userId ambigus colum name
    bd=database()
    return [{"recordId": entry[0],
             "createdDate": entry[1],
             "bed": entry[2],
             "pacientDocument": entry[3],
             "pacientLastName": entry[4],
             "comment": entry[5],
             "nurseId": entry[6],
             "auxNurseId": entry[7],
             "sectorId": entry[8],
             "roomId": entry[9],
             "SectorName": entry[10],
             "roomName": entry[11],
             "nurseName": entry[12],
             "nurseLastName": entry[13]
             } for entry in bd.run_sql(sql_sentence)]