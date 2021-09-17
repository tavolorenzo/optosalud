from data.databases.conectDB import database as bd

def create_role(roleDescription, access):
    sql_sentence = f"""
    INSERT INTO role(roleDescription, access) 
    VALUE ('{roleDescription}','{access}')
    """
    bd.run_sql(sql_sentence)

def update_role(roleId, roleDescription, access):
    sql_sentence = f"""
    UPDATE role SET roleDescription='{roleDescription}', access='{access}'
    WHERE roleId='{roleId}'
    """
    bd.run_sql(sql_sentence)

def view_role(roleId):
    sql_sentence = f"""
    SELECT * FROM role
    WHERE roleId='{roleId}'
    """
    roleInfo=bd.run_sql(sql_sentence)
    return roleInfo