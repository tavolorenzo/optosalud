from data.databases.conectDB import database as bd

def create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId):
    sql_sentence = f"""
        INSERT INTO USER(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId) 
        VALUES ('{document}', '{name}', '{lastName}', '{phone}', '{email}', '{photoURI}', '{password}', '{jobPosition}', '{roleId}')
    """
    bd.run_sql(sql_sentence)

