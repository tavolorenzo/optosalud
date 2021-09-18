from data.databases.connectDB import database as bd

def create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId):
    sql_sentence = f"""
        INSERT INTO USER(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId) 
        VALUES ('{document}', '{name}', '{lastName}', '{phone}', '{email}', '{photoURI}', '{password}', '{jobPosition}', '{roleId}')
    """
    bd.run_sql(sql_sentence)


def update_user(userId, phone, email, photoURI,password, jobPosition, roleId, status):
    sql_sentence = f"""
       UPDATE user SET phone='{phone}', email='{email}', photoURI='{photoURI}',password='{password}', jobPosition='{jobPosition}', roleId='{roleId}', status='{status}'
       WHERE userId='{userId}'
    """
    bd.run_sql(sql_sentence)

def view_user_by_document(document):
    sql_sentence = f"""
    SELECT userId FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE document='{document}'  
    """
    userInfo=bd.run_sql(sql_sentence)
    return userInfo

def view_user_by_id(userId):
    sql_sentence = f"""
    SELECT * FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE userId='{userId}'  
    """
    userInfo=bd.run_sql(sql_sentence)
    return userInfo

def search_users_by_jobPosition(jobPosition):
    sql_sentence = f"""
    SELECT * FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE jobPosition='{jobPosition}'  
    """
    userInfo=bd.run_sql(sql_sentence)
    return userInfo

def login_user(document):
    sql_sentence = f"""
    SELECT password FROM user
    WHERE document='{document}'    
    """
    userInfo=bd.run_sql(sql_sentence)
    return userInfo