from data.databases.conectDB import database as bd

def create_room(rooms, sectorId):
    for item in rooms:
        sql_sentence = f"""
        INSERT INTO room (name, sectorId) 
        VALUES ('{rooms["name"]}','{sectorId}')
        """
        bd.run_sql(sql_sentence)
    
'''
def search_room_by_sector(sectorId):
    sql_sentence = f"""
    SELECT * FROM room WHERE sectorId='{sectorId}'  
    """
    roomsInfo=bd.run_sql(sql_sentence)
    return roomsInfo
'''

def update_room(rooms,sectorId):
    for item in rooms:
        try: 
            sql_sentence = f"""
            UPDATE room SET name='{rooms["name"]}', status='{rooms["status"]}' 
            WHERE roomId='{rooms["roomId"]}'
            """
            bd.run_sql(sql_sentence)
        except:
            sql_sentence = f"""
            INSERT INTO room (name, sectorId) 
            VALUES ('{rooms["name"]}','{sectorId}')
            """
            bd.run_sql(sql_sentence)