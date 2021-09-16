from data.databases.conectDB import database as bd
from data.models import room

def create_sector(name, photoURI, roomName):
    sql_sentence = f"""
        INSERT INTO SECTOR(name, photoURI) 
        VALUES ('{name}', '{photoURI}')
    """
    bd.run_sql(sql_sentence)
    sql_sentence = f"""
        SELECT sectorId FROM SECTOR WHERE name="{name}"
        """
    sectorId=bd.run_sql(sql_sentence)
    room.create_room(roomName,sectorId)