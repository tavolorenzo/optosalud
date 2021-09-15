from data.databases.conectDB import database as bd

def create_room(name):
    sql_sentence = f"""
        INSERT INTO ROOM(name) 
        VALUES ('{name}')
    """
    bd.run_sql(sql_sentence)