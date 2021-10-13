from data.models import user as user_model

def create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId): #OK
    user_model.create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId)

def update_user(userId, phone, email, photoURI,password, jobPosition, roleId, status): #OK
    user_model.update_user(userId, phone, email, photoURI,password, jobPosition, roleId, status)

def view_user_by_document(document): #OK 
    return user_model.view_user_by_document(document)

def view_user_by_id(userId): #OK
    return user_model.view_user_by_id(userId)

def search_users_by_jobPosition(jobPosition): #OK
    return user_model.search_users_by_jobPosition(jobPosition)