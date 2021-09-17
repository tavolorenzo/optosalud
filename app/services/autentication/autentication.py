from data.models import user as user_model

def login(document):
    user_model.login_user(document)
