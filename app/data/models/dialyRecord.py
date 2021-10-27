from data.databases.connectDB import database 

def create_dialyRecord(sectorId,roomId,auxNurseId, nurseId, bed, pacientDocument, pacientName, pacientLastName, comment): #OK
    sql_sentence = f"""
        INSERT INTO dialyRecord(sectorId,roomId,auxNurseId, nurseId,  bed, pacientDocument, pacientName, pacientLastName, comment)
        VALUES ('{sectorId}','{roomId}','{auxNurseId}', '{nurseId}', '{bed}', '{pacientDocument}', '{pacientName}', '{pacientLastName}', '{comment}')
    """
    bd=database()
    bd.run_sql(sql_sentence)

def view_dialyRecord(recordId): #OK
    sql_sentence = f"""
    SELECT dialyRecord.*, sector.name AS SectorName, room.name AS RoomName 
    FROM dialyRecord
    INNER JOIN sector ON dialyRecord.sectorId=sector.sectorId
    INNER JOIN room ON dialyRecord.roomId=room.roomId
    WHERE recordId='{recordId}'
    """
    bd=database()
    dialyRecordInfo= bd.run_sql(sql_sentence)
    sql_sentence = f"""
    SELECT dialyRecord.nurseId AS nurseId, 
    user.name AS nurseName, user.lastName AS nurseLastName
    FROM dialyRecord
    INNER JOIN user ON dialyRecord.nurseId=user.userId 
    WHERE recordId='{recordId}'
    """
    nurseInfo= bd.run_sql(sql_sentence)
    sql_sentence = f"""
    SELECT dialyRecord.auxNurseId AS auxNurseId, 
    user.name AS AuxNurseName, user.lastName AS AuxNurseLastName
    FROM dialyRecord
    INNER JOIN user ON dialyRecord.auxNurseId=user.userId 
    WHERE recordId='{recordId}'
    """
    auxNurseInfo= bd.run_sql(sql_sentence)
    return [{"recordId": entry[0],
             "createdDate": entry[1],
             "bed": entry[2],
             "pacientDocument": entry[3],
             "pacientName": entry[4],
             "pacientLastName": entry[5],
             "coment": entry[6],
             "nurseInfo":[{
                "nurseId":entry[0],
                "nurseName": entry[1],
                "nurseLastName": entry[2]
             }  for entry in nurseInfo],
             "auxNurseInfo":[{
                "auxNurseId":entry[0],
                "auxNurseName": entry[1],
                "auxNurseLastName": entry[2]
             }  for entry in auxNurseInfo],
             "sectorId": entry[9],
             "SectorName": entry[11],
             "roomId": entry[10],
             "roomName": entry[12],
             } for entry in dialyRecordInfo]

def view_dialyRecords(): #OK
    sql_sentence = f"""
    SELECT dialyRecord.*, sector.name AS SectorName, room.name AS RoomName 
    FROM dialyRecord
    INNER JOIN sector ON dialyRecord.sectorId=sector.sectorId
    INNER JOIN room ON dialyRecord.roomId=room.roomId
    """
    bd=database()
    dialyRecordInfo= bd.run_sql(sql_sentence)
    
    return [{"recordId": entry[0],
             "createdDate": entry[1],
             "bed": entry[2],
             "pacientDocument": entry[3],
             "pacientName": entry[4],
             "pacientLastName": entry[5],
             "comment": entry[6],
             "nurseId":entry[7],
             "auxNurseId":entry[8],
             "sectorId": entry[9],
             "SectorName": entry[11],
             "roomId": entry[10],
             "roomName": entry[12],
             } for entry in dialyRecordInfo]