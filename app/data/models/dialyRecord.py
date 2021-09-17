from data.databases.connectDB import database as bd

def create_dialyRecord(sectorId,roomId,auxNurseId, nurseId, createdDate, bed, pacientDocument, pacientName, pacientLastName, comment):
    sql_sentence = f"""
        INSERT INTO dialyRecord(sectorId,roomId,auxNurseId, nurseId, createdDate, bed, pacientDocument, pacientName, pacientLastName, comment)
        VALUES ('{sectorId}','{roomId}','{auxNurseId}', '{nurseId}', '{createdDate}', '{bed}', '{pacientDocument}', '{pacientName}', '{pacientLastName}', '{comment}')
    """
    bd.run_sql(sql_sentence)

def view_dialyRecord(recordId):
    sql_sentence = f"""
    SELECT * FROM dialyRecord 
    INNER JOIN sector ON dialyRecord.sectorId=sector.sectorId
    INNER JOIN room ON dialyRecord.roomId=room.roomId
    INNER JOIN user ON dialyRecord.nurseId=user.userId
    INNER JOIN user ON dialyRecord.auxNurseId=user.userId
    WHERE recordId='{recordId}'
    """
    dialyRecordInfo=bd.run_sql(sql_sentence)
    return dialyRecordInfo