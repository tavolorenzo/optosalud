from flask import Flask, request, jsonify
from services.user import user
from services.task import task
from services.role import role
from services.sector import sector
from services.autentication import autentication
from services.dialyRecord import dialyRecord

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    login_info=request.get_json()
    if 'document' not in login_info:
        return 'El decumento de usuario es requerido', 412
    if 'password' not in login_info:
        return 'La clave es requerida', 412 
    try:
        autentication.login(login_info['document'])
        return 'OK', 200
    except Exception:
        return 'El usuario no esta registrado o autorizado', 412 

@app.route('/logout',methods=['DELETE'])
#DEFINIR FUCION 

@app.route('/users',methods=['GET'])
def get_user_id():
    user_document=request.get_json()
    try:
        users_info=user.view_user_by_document(user_document['document'])
        return jsonify(users_info)
    except Exception:
        return 'Usuario no encontrado', 404

@app.route('/users/search',methods=['GET'])
def get_users_by_jobPosition():
    user_jobPosition=request.get_json()
    try:
        users_info=user.search_users_by_jobPosition(user_jobPosition['jobPosition'])
        return jsonify(users_info)
    except Exception:
        return 'No se encontraron usuarios', 404

@app.route('/users/<userId>',methods=['GET'])
def view_user(user_id):
    try:
        user_info=user.view_user_by_id(user_id)
        return jsonify(user_info)
    except Exception:
        return 'Usuario no encontrado', 404

@app.route('/users/new',methods=['POST'])
def create_users():
    user_info = request.get_json()
    if 'document' not in user_info:
        return 'El decumento de usuario es requerido', 412
    if 'name' not in user_info:
        return 'El nombre de usuario es requerido', 412
    if 'lastName' not in user_info:
        return 'El apellido de usuario es requerido', 412
    if 'phone' not in user_info:
        return 'El telefono de usuario es requerido', 412
    if 'email' not in user_info:
        return 'El email de usuario es requerido', 412
    if 'photoURI' not in user_info:
        user_info.update({'phtoURI':'imagens/usericon.png'})
    if 'jobPosition' not in user_info:
        return 'El puesto de trabajo de usuario es requerido', 412
    if 'roleId' not in user_info:
        return 'La rol de usuario es requerida', 412
    if 'password' not in user_info:
        return 'La clave es requerida', 412 
    try:
        user.create_user(user_info['document'], user_info['name'], user_info['lastname'], user_info['phone'], user_info['email'], user_info['photoURI'], user_info['password'], user_info['jobposition'], user_info['roleId'])
        return 'OK', 200
    except Exception:
        return 'Le usuario ya existe', 412 

@app.route('/users/<userId>',methods=['PUT'])
def update_user(userId):
    user_info = request.get_json()
    if 'phone' not in user_info:
        return 'El telefono de usuario es requerido', 412
    if 'email' not in user_info:
        return 'El email de usuario es requerido', 412
    if 'photoURI' not in user_info:
        user_info.update({'phtoURI':'imagens/usericon.png'})
    if 'jobPosition' not in user_info:
        return 'El puesto de trabajo de usuario es requerido', 412
    if 'password' not in user_info:
        return 'La clave  de usuario es requerida', 412
    if 'roleId' not in user_info:
        return 'La rol de usuario es requerida', 412
    if 'status' not in user_info:
        return 'La status de usuario es requerida', 412
    try:
        user.update_user(userId, user_info['phone'], user_info['email'], user_info['photoURI'], user_info['password'], user_info['jobPostion'], user_info['roleId'], user_info['status'])
        return 'OK', 200
    except Exception:
        return 'No se encontro el usuario'
    

@app.route('/tasks/new',methods=['POST'])
def create_task():
    task_info = request.get_json()
    if 'roleId' not in task_info:
        return 'El campo rol es requerido', 412
    if 'title' not in task_info:
        return 'El titulo es requerido', 412
    task.create_task(task_info['roleId'], task_info['title'])
    return 'OK', 200
 
  
@app.route('/tasks/{taskId}',methods=['GET'])
def view_task(taskId):
    try:
        task_info = task.view_task(taskId)
        return jsonify(task_info)
    except Exception:
        return 'La tarea no se ha encontrado', 404

@app.route('/tasks/{roleId}',methods=['GET'])
def view_task_by_role(roleId):
    try:
        tasks_info = task.view_task_by_role(roleId)
        return jsonify(tasks_info)
    except Exception:
        return 'No se han encontrado tareas', 404

@app.route('/roles/new',methods=['POST'])
def create_role():
    role_info=request.get_json()
    if 'description' not in role_info:
        return "La desscripcion del rol es requeria", 412
    if 'access' not in role_info:
        return "La acceso del rol es requeria", 412
    role.create_role


@app.route('/dialy_records/new',methods=['POST'])
def create_dialyRecord():
    dialyRecord_info=request.get_json()
    if 'sectorId' not in dialyRecord_info:
        return 'El sector es requerido', 412
    if 'roomId' not in dialyRecord_info:
        return 'La habitacion es requerida', 412
    if 'auxNurseId' not in dialyRecord_info:
        return 'Puesto de trabajo requerido', 412 
    if 'nurseId' not in dialyRecord_info:
        return 'Puesto de trabajo requerido', 412
    if 'createdDate' not in dialyRecord_info:
        return 'La fecha y hora es requerida', 412  
    if 'bed' not in dialyRecord_info:
        return 'cama requerida', 412
    if 'pacientdocument' not in dialyRecord_info:
        return 'Documento del paciente requerido', 412   
    if 'pacientname' not in dialyRecord_info:
        return 'Nombre del paciente requerido', 412
    if 'pacientlastname' not in dialyRecord_info:
        return 'Apellido del paciente requerido', 412   
    if 'comment' not in dialyRecord_info:
        return 'Comentario requerido', 412        
    dialyRecord.create_dialyRecord(dialyRecord_info['sectorId'], dialyRecord_info['roomId'], dialyRecord_info['auxNurseId'], dialyRecord_info['nurseId'], dialyRecord_info['createdDate'], dialyRecord_info['bed'], dialyRecord_info['pacientDocument'], dialyRecord_info['pacientName'], dialyRecord_info['pacientLastName'],dialyRecord_info['comment'])
    return 'OK', 200


@app.route('/dialy_records/<recordId>',methods=['GET'])
def view_dialyRecord(recordId):
    try:
        dialyRecord_info =dialyRecord.view_dialyRecord(recordId)
        return jsonify(dialyRecord_info)
    except Exception:
        return 'Registro no encontrado', 404


@app.route('/dialy_records',methods=['GET'])
def view_dialyRecords():
    dialyRecord_info =dialyRecord.view_dialyRecords()
    return jsonify(dialyRecord_info)

"""
@app.route('/sectors/new',methods=['POST'])
#DEFINIR FUCION

@app.route('/sectors/<sectorId>',methods=['PUT'])
#DEFINIR FUCION

@app.route('/sectors/<sectorId>',methods=['GET'])
#DEFINIR FUCION

@app.route('/sectors',methods=['GET'])
#DEFINIR FUCION

@app.route('/sectors/search',methods=['GET'])
#DEFINIR FUCION

@app.route('/<sectorId>/rooms',methods=['GET'])
#DEFINIR FUCION

@app.route('/phramac_records/new',methods=['POST'])
#DEFINIR FUCION

@app.route('/pahrmac_records/{recordId}',methods=['GET'])
#DEFINIR FUCION

@app.route('/pahrmac_records',methods=['GET'])
#DEFINIR FUCION

@app.route('/material_records/new',methods=['POST'])
#DEFINIR FUCION

@app.route('/material_records/{recordId}',methods=['GET'])
#DEFINIR FUCION

@app.route('/material_records',methods=['GET'])
#DEFINIR FUCION 
"""

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
