from data.databases.connectDB import database as bd

def create_task(roleId, title):
    sql_sentence = f"""
        INSERT INTO TASK(roleId, title) 
        VALUES ('{roleId}', '{title}')
    """
    bd.run_sql(sql_sentence)

def update_task(taskId, title):
    sql_sentence = f"""
        UPDADE task SET title='{title}' WHERE taskId='{taskId}'
    """
    bd.run_sql(sql_sentence)

def view_task(taskId):
    sql_sentence = f"""
    SELECT * FROM task WHERE taskId='{taskId}'  
    """
    taskInfo=bd.run_sql(sql_sentence)
    return taskInfo

def view_task_by_role(roleId):
    sql_sentence = f"""
    SELECT * FROM task 
    INNER JOIN role ON task.roleId=role.roleId
    WHERE roleId='{roleId}'  
    """
    taskInfo=bd.run_sql(sql_sentence)
    return taskInfo