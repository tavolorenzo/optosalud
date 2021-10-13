from data.databases.connectDB import database

def create_role(roleDescription, access): #OK
    sql_sentence = f"""
    INSERT INTO role(roleDescription, access) 
    VALUES ('{roleDescription}','{access}')
    """
    bd=database()
    bd.run_sql(sql_sentence)

def update_role(roleId, roleDescription, access): #OK
    sql_sentence = f"""
    UPDATE role SET roleDescription='{roleDescription}', access='{access}'
    WHERE roleId='{roleId}'
    """
    bd=database()
    bd.run_sql(sql_sentence)

def view_role(roleId): #OK
    sql_sentence = f"""
    SELECT * FROM role
    WHERE roleId='{roleId}'
    """
    bd=database()
    return [{"roleId": entry[0],
             "description": entry[1],
             } for entry in bd.run_sql(sql_sentence)]