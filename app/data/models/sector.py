from data.databases.connectDB import database as bd
from models import room

def create_sector(name, photoURI, rooms):
    sql_sentence = f"""
        INSERT INTO SECTOR(name, photoURI) 
        VALUES ('{name}', '{photoURI}')
    """
    bd.run_sql(sql_sentence)
    sql_sentence = f"""
        SELECT sectorId FROM SECTOR WHERE name="{name}"
    """
    sectorId=bd.run_sql(sql_sentence)
    room.create_room(rooms,sectorId['sectorId'])

def update_sector(sectorId, name, photoURI, status, rooms):
    sql_sentence = f"""
        UPDATE sector SET name='{name}', photoURI='{photoURI}', status='{status}'
        WHERE sectorId='{sectorId}'
    """
    bd.run_sql(sql_sentence)
    room.update_room(rooms,sectorId)

def view_sector(sectorId):
    sql_sentence=f"""
        SELECT * FROM sector 
        INNER JOIN room ON sector.sectorId=room.sectorId
    """
    sectorInfo = bd.run_sql(sql_sentence)
    return sectorInfo
