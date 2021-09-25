from data.databases.connectDB import database

def create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId):
    sql_sentence = f"""
        INSERT INTO USER(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId) 
        VALUES ('{document}', '{name}', '{lastName}', '{phone}', '{email}', '{photoURI}', '{password}', '{jobPosition}', '{roleId}')
    """
    bd=database()
    bd.run_sql(sql_sentence)


def update_user(userId, phone, email, photoURI,password, jobPosition, roleId, status):
    sql_sentence = f"""
       UPDATE user SET phone='{phone}', email='{email}', photoURI='{photoURI}',password='{password}', jobPosition='{jobPosition}', roleId='{roleId}', status='{status}'
       WHERE userId='{userId}'
    """
    bd=database()
    bd.run_sql(sql_sentence)

def view_user_by_document(document):
    sql_sentence = f"""
    SELECT userId FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE document='{document}'  
    """
    bd=database()
    return [{"userID": entry[0],
             "document": entry[1],
             "name": entry[2],
             "lastName": entry[3],
             "photoURI": entry[4],
             "phone": entry[5],
             "jobPosition": entry[6],
             "email": entry[7],
             "status": entry[8],
             "roleId": entry[9],
             "roleDescription": entry[10],
             } for entry in bd.run_sql(sql_sentence)]

def view_user_by_id(userId):
    sql_sentence = f"""
    SELECT user.*, role.roleDescription
    FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE userId='{userId}'  
    """
    bd=database()
    return [{"userID": entry[0],
             "document": entry[1],
             "name": entry[2],
             "lastName": entry[3],
             "photoURI": entry[4],
             "phone": entry[5],
             "jobPosition": entry[6],
             "email": entry[7],
             "status": entry[8],
             "roleId": entry[9],
             "roleDescription": entry[10],
             } for entry in bd.run_sql(sql_sentence)]

def search_users_by_jobPosition(jobPosition):
    sql_sentence = f"""
    SELECT user.*, role.roleDescription
    FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE jobPosition='{jobPosition}'  
    """
    bd=database()
    return  [{"userID": entry[0],
             "document": entry[1],
             "name": entry[2],
             "lastName": entry[3],
             "photoURI": entry[4],
             "phone": entry[5],
             "jobPosition": entry[6],
             "email": entry[7],
             "status": entry[8],
             "roleId": entry[9],
             "roleDescription": entry[10],
             } for entry in bd.run_sql(sql_sentence)]

def login_user(document):
    sql_sentence = f"""
    SELECT password FROM user
    WHERE document='{document}'    
    """
    bd=database()
    return [{"password": entry[0]
             } for entry in bd.run_sql(sql_sentence)]