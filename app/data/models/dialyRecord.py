from data.databases.conectDB import database as bd

def create_dialyRecord(sectorId,roomId,auxNurseId, nurseId, createdDate, bed, pacientDocument, pacientName, pacientLastName, comment):
    sql_sentence = f"""
        INSERT INTO dialyRecord(sectorId,roomId,auxNurseId, nurseId, createdDate, bed, pacientDocument, pacientName, pacientLastName, comment)
        VALUES ('{sectorId}','{roomId}','{auxNurseId}', '{nurseId}', '{createdDate}', '{bed}', '{pacientDocument}', '{pacientName}', '{pacientLastName}', '{comment}')
    """
    bd.run_sql(sql_sentence)