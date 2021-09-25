from data.databases.connectDB import database
from data.models import room

def create_sector(name, photoURI, rooms):
    sql_sentence = f"""
        INSERT INTO SECTOR(name, photoURI) 
        VALUES ('{name}', '{photoURI}')
    """
    bd=database()
    sectorId=bd.run_sql(sql_sentence,True)
    room.create_room(rooms,sectorId)

def update_sector(sectorId, name, photoURI, status, rooms):
    sql_sentence = f"""
        UPDATE sector SET name='{name}', photoURI='{photoURI}', status='{status}'
        WHERE sectorId='{sectorId}'
    """
    bd=database()
    bd.run_sql(sql_sentence)
    room.update_room(rooms,sectorId)

def view_sector(sectorId):
    sql_sentence=f"""
        SELECT * FROM sector 
        INNER JOIN room ON sector.sectorId=room.sectorId
        WHERE sectorId='{sectorId}'
    """
    bd=database()
    sectorInfo = bd.run_sql(sql_sentence)
    return sectorInfo

def view_sectors():
    sql_sentence=f"""
        SELECT * FROM sector 
        INNER JOIN room ON sector.sectorId=room.sectorId
    """
    bd=database()
    sectorsInfo = bd.run_sql(sql_sentence)
    return sectorsInfo

def search_sectorId_ny_name(name):
    sql_sentence=f"""
        SELECT sectorId FROM sector
        WHERE name='{name}'
    """
    bd=database()
    sectorInfo=bd.run_sql(sql_sentence)
    return sectorInfo
