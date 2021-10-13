from data.databases.connectDB import database

def create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId): #OK
    sql_sentence = f"""
        INSERT INTO USER(document, name, lastName, phone, email, photoURI, password, jobPosition, roleId) 
        VALUES ('{document}', '{name}', '{lastName}', '{phone}', '{email}', '{photoURI}', '{password}', '{jobPosition}', '{roleId}')
    """
    bd=database()
    bd.run_sql(sql_sentence)


def update_user(userId, phone, email, photoURI,password, jobPosition, roleId, status): #OK
    sql_sentence = f"""
       UPDATE user SET phone='{phone}', email='{email}', photoURI='{photoURI}',password='{password}', jobPosition='{jobPosition}', roleId='{roleId}', status='{status}'
       WHERE userId='{userId}'
    """
    bd=database()
    bd.run_sql(sql_sentence)

def view_user_by_document(document): #OK
    sql_sentence = f"""
    SELECT userId FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE document='{document}'  
    """
    bd=database()
    return [{"userId": entry[0],
             } for entry in bd.run_sql(sql_sentence)]

def view_user_by_id(userId): #OK
    sql_sentence = f"""
    SELECT user.*, role.roleDescription
    FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE userId='{userId}'  
    """
    bd=database()
    return [{"userId": entry[0],
             "document": entry[1],
             "name": entry[2],
             "lastName": entry[3],
             "photoURI": entry[4],
             "phone": entry[5],
             "jobPosition": entry[6],
             "email": entry[7],
             "password": entry[8],
             "status": entry[9],
             "roleId": entry[10],
             "roleDescription": entry[11],
             } for entry in bd.run_sql(sql_sentence)]

def search_users_by_jobPosition(jobPosition): #OK
    sql_sentence = f"""
    SELECT user.*, role.roleDescription
    FROM user
    INNER JOIN role ON role.roleId=role.roleId
    WHERE jobPosition='{jobPosition}'  
    """
    bd=database()
    return  [{"userId": entry[0],
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

def login_user(document,password): #OK
    sql_sentence = f"""
    SELECT userId, name, lastName, roleId FROM user
    WHERE document='{document}' and password ='{password}'
    """
    bd=database()
    return [{"id": entry[0],
             "name": entry[1],
             "lastName": entry[2],
             "roleId": entry[3]
             } for entry in bd.run_sql(sql_sentence)]

def create_session(user_id, dt_string): #OK
    sql_sentence = f"""
               INSERT INTO SESSIONS(userId, date)
               VALUES ('{user_id}', '{dt_string}')
           """
    bd = database()
    return  bd.run_sql(sql_sentence, True)

def get_session(id):
    sql_sentence = f"""
        SELECT id, userId, date
        FROM sessions WHERE id = {id}
    """
    bd = database()
    return [{"id": entry[0],
             "userId": entry[1],
             "date": entry[2]}
            for entry in bd.run_sql(sql_sentence)]
