from data.models import user as user_model
from datetime import datetime

def valid_user(document,password): #OK
    userInfo =user_model.login_user(document,password)
    return not len(userInfo) == 0

def create_session(userId): #OK
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return user_model.create_session(userId, dt_string)

def login(document,password): # OK
    if valid_user(document,password):
        user = user_model.login_user(document,password)[0]
        return create_session(user['id'])
    else:
        raise Exception("El usuario no existe o la clave es invalida")

def valid_session(session_id):
    sessiones = user_model.get_session(session_id)
    if len(sessiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sessiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Sesion expirada
        return False
    else:
        return True
