from data.databases.conectDB import database as bd

def create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId):
    sql_sentence = f"""
        INSERT INTO USER(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId) 
        VALUES ('{document}', '{name}', '{lastName}', '{phone}', '{email}', '{photoURI}', '{password}', '{jobPosition}', '{roleId}')
    """
    bd.run_sql(sql_sentence)


def update_user(phone, email, photoURI,password, jobPosition, roleId, status):
    sql_sentence = f"""
        
    """
    bd.run_sql(sql_sentence)

def view_user(document):
    sql_sentence = f"""
    SELECT * FROM user WHERE document='{document}'  
    """
    userInfo=bd.run_sql(sql_sentence)
    return userInfo

def search_user_by_jobPosition(jobPosition):
    sql_sentence = f"""
    SELECT * FROM user WHERE jobPosition='{jobPosition}'  
    """
    userInfo=bd.run_sql(sql_sentence)
    return userInfo

