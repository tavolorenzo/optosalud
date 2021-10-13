from os import name
from data.databases.connectDB import database

def create_room(rooms, sectorId): #OK
        for room in rooms:
                sql_sentence = f"""
                INSERT INTO room (name, sectorId) 
                VALUES ('{room}','{sectorId}')
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

def update_room(rooms,sectorId): #OK
        for  room in rooms:
                sql_sentence = f"""
                SELECT roomId FROM room
                WHERE sectorId='{sectorId}' AND name='{room}'
                """
                bd=database()
                roomId=bd.run_sql(sql_sentence) 
                if roomId == []:
                        sql_sentence = f"""
                        INSERT INTO room (name, sectorId) 
                        VALUES ('{room}','{sectorId}')
                        """
                        bd=database()
                        bd.run_sql(sql_sentence)


