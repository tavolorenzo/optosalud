from data.models import task as task_model

def create_task(roleId, title):
    task_model.create_task(roleId, title)

def update_task(taskId, title):
    task_model.update_task(taskId, title)

def view_task(taskId):
    task_model.view_task(taskId)

def view_task_by_role(roleId):
    task_model.view_task_by_role(roleId)
