from data.databases.conectDB import database as bd

def create_role(roleDescription, access):
    sql_sentence = f"""
    INSERT INTO role(roleDescription, access) 
    VALUE ('{roleDescription}','{access}')
    """
    bd.run_sql(sql_sentence)