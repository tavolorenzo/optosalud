from data.databases.connectDB import database 

def create_task(roleId, description): #OK
    sql_sentence = f"""
        INSERT INTO TASK(roleId, description) 
        VALUES ('{roleId}', '{description}')
    """
    bd=database()
    bd.run_sql(sql_sentence)

def update_task(taskId, description):
    sql_sentence = f"""
        UPDADE task SET description='{description}' WHERE taskId='{taskId}'
    """
    bd=database()
    bd.run_sql(sql_sentence)

def view_task(taskId): #OK
    sql_sentence = f"""
    SELECT task.*, role.roleDescription 
    FROM task 
    INNER JOIN role ON task.roleId=role.roleId
    WHERE taskId='{taskId}'  
    """
    bd=database()
    return [{"taskId": entry[0],
             "description": entry[1],
             "roleId": entry[2],
             "roleDescription": entry[3],
             } for entry in bd.run_sql(sql_sentence)]

def view_task_by_role(roleId): #OK
    sql_sentence = f"""
    SELECT *
    FROM task 
    WHERE roleId='{roleId}'  
    """
    bd=database()
    return [{"taskId": entry[0],
             "description": entry[1],
             "roleId": entry[2],
            } for entry in bd.run_sql(sql_sentence)]