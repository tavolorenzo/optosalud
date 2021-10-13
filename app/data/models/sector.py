from data.databases.connectDB import database
from data.models import room

def create_sector(name, photoURI, rooms): #OK
    sql_sentence = f"""
        INSERT INTO SECTOR(name, photoURI) 
        VALUES ('{name}', '{photoURI}')
    """
    bd=database()
    sectorId=bd.run_sql(sql_sentence,True)
    room.create_room(rooms,sectorId)
    

def update_sector(sectorId, name, photoURI, status,rooms): #OK
    sql_sentence = f"""
        UPDATE sector SET name='{name}', photoURI='{photoURI}', status='{status}'
        WHERE sectorId='{sectorId}'
    """
    bd=database()
    bd.run_sql(sql_sentence)
    room.update_room(rooms,sectorId)

def view_sector(sectorId): #OK
    sql_sentence=f"""
        SELECT *
        FROM sector 
        WHERE sectorId='{sectorId}'
    """
    bd=database()
    sectorInfo = bd.run_sql(sql_sentence)
    sql_sentence=f"""
        SELECT roomId, name, status
        FROM room
        WHERE sectorId='{sectorId}'
    """
    bd=database()
    roomsInfo = bd.run_sql(sql_sentence)
    return [{"sectorId": entry[0],
             "name": entry[1],
             "photoURI": entry[2],
             "status": entry[3],
             "rooms":[{"roomId": entry[0],
                        "name": entry[1],
                        "status": entry[2]
                    }for entry in roomsInfo]
             } for entry in sectorInfo]

def view_sectors():  #OK
    sql_sentence=f"""
        SELECT * FROM sector 
    """
    bd=database()
    sectorsInfo = bd.run_sql(sql_sentence)
    return [{"sectorId": entry[0],
             "name": entry[1],
             "photoURI": entry[2],
             "status": entry[3]
             } for entry in sectorsInfo]

def search_sectorId_ny_name(name): #OK
    sql_sentence=f"""
        SELECT sectorId FROM sector
        WHERE name='{name}'
    """
    bd=database()
    sectorInfo=bd.run_sql(sql_sentence)
    return [{"sectorId": entry[0]
             } for entry in sectorInfo]
