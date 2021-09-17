from data.models import user as user_model

def create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId):
    user_model.create_user(document, name, lastName, phone, email, photoURI,password, jobPosition, roleId)

def update_user(userId, phone, email, photoURI,password, jobPosition, roleId, status):
    user_model.update_user(userId, phone, email, photoURI,password, jobPosition, roleId, status)

def view_user(document):
    user_model.view_user(document)

def search_user_by_jobPosition(jobPosition):
    user_model.search_user_by_jobPosition(jobPosition)

