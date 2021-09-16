from data.databases.conectDB import database as bd
from data.models import material

def create_materialRecord(sectorId,roomId,auxNurseId, nurseId, createdDate, materialName, comment, quantity, unit):
    sql_sentence = f"""
        INSERT INTO materialRecord(sectorId,roomId,auxNurseId, nurseId) 
        VALUES ('{sectorId}','{roomId}','{auxNurseId}', '{nurseId}', '{createdDate}')
    """
    bd.run_sql(sql_sentence)
    sql_sentence = f"""
        SELECT recordId FROM materialRecord WHERE createdDate="{createdDate}" AND auxNurseId='{nurseId}'
        """
    recordId=bd.run_sql(sql_sentence)
    material.create_material(recordId, materialName, comment, quantity, unit)
    bd.run_sql(sql_sentence)