from data.databases.conectDB import database as bd
from data.models import drug

def create_pharmacRecord(sectorId,roomId,auxNurseId, nurseId, createdDate,drugName, pharmaceuticalForm, quantity, unit,):
    sql_sentence = f"""
        INSERT INTO pharmacRecord(sectorId,roomId,auxNurseId, nurseId) 
        VALUES ('{sectorId}','{roomId}','{auxNurseId}', '{nurseId}', '{createdDate}')
    """
    bd.run_sql(sql_sentence)
    sql_sentence = f"""
        SELECT recordId FROM pharmacRecord WHERE createdDate="{createdDate}" AND auxNurseId='{nurseId}'
        """
    recordId=bd.run_sql(sql_sentence)
    drug.create_drug(recordId, drugName, pharmaceuticalForm, quantity, unit)
    bd.run_sql(sql_sentence)