from data.databases.conectDB import database as bd

def create_task(roleId, title):
    sql_sentence = f"""
        INSERT INTO TASK(roleId, title) 
        VALUES ('{roleId}', '{title}')
    """
    bd.run_sql(sql_sentence)