from data.databases.conectDB import database as bd

def create_room(name, sectorId):
    sql_sentence = f"""
    INSERT INTO ROOM(name, sectorId) 
    VALUES ('{name}','{sectorId}')
    """
    bd.run_sql(sql_sentence)