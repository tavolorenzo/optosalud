from data.databases.connectDB import database

def create_room(rooms, sectorId):
    for room in rooms():    
        sql_sentence = f"""
        INSERT INTO room (name, sectorId) 
        VALUES ('{room["name"]}','{sectorId}')
        """
        bd=database()
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
    for room in rooms:
        try: 
            sql_sentence = f"""
            UPDATE room SET name='{room["name"]}', status='{room["status"]}' 
            WHERE roomId='{room["roomId"]}'
            """
            bd=database()
            bd.run_sql(sql_sentence)
        except Exception:
            sql_sentence = f"""
            INSERT INTO room (name, sectorId) 
            VALUES ('{rooms["name"]}','{sectorId}')
            """
            bd=database()
            bd.run_sql(sql_sentence)