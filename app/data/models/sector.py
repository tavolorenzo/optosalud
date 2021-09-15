from data.databases.conectDB import database as bd
from data.models.sector import create_room as room

def create_sector(name, photoURI, roomName):
    sql_sentence = f"""
        INSERT INTO SECTOR(name, photo) 
        VALUES ('{name}', '{photoURI}')
    """
    sql_sentence = f"""
        SELECT FROM SECTOR(sectorId) 
        WHERE (name='{name}')
    """
    bd.run_sql(sql_sentence)