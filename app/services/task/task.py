from data.models import task as task_model

def create_task(roleId, description): #OK
    task_model.create_task(roleId, description)

def update_task(taskId, description):
    task_model.update_task(taskId, description)

def view_task(taskId): #OK
    return task_model.view_task(taskId)

def view_task_by_role(roleId): #OK
    return task_model.view_task_by_role(roleId)
