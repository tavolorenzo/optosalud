from flask import Flask, request, jsonify, render_template
from services.user import user
from services.task import task
from services.role import role
from services.sector import sector
from services.autentication import autentication
from services.dialyRecord import dialyRecord

app = Flask(__name__)

@app.route('/login',methods=['POST']) #OK CREA LA SESSION EN BD 
def login():
    login_info=request.get_json()
    if 'document' not in login_info:
        return 'El documento de usuario es requerido', 412
    if 'password' not in login_info:
        return 'La clave es requerida', 412 
    try:
        autentication.login(login_info['document'],login_info['password'])
        return 'OK', 200
    except Exception:
        return "El usuario o clave son incorrectos", 404

@app.route('/logout',methods=['DELETE'])
#DEFINIR FUCION 

@app.route('/users',methods=['GET']) #OK DEVUELVE USER ID SEGUN DOCUMENTO
def get_user_id():
    user_document=request.get_json()
    try:
        users_info=user.view_user_by_document(user_document['document'])
        return jsonify(users_info)
    except Exception:
        return 'Usuario no encontrado', 404

@app.route('/users/search',methods=['GET']) #OK DEVUELVE USER.* y ROLE.* SEGUN JOBPOSIITON
def get_users_by_jobPosition():
    user_jobPosition=request.get_json()
    try:
        users_info=user.search_users_by_jobPosition(user_jobPosition['jobPosition'])
        return jsonify(users_info)
    except Exception:
        return 'No se encontraron usuarios', 404

@app.route('/users/<userId>',methods=['GET']) #OK DEVUELVE USER.* y ROLE.* SEGUN USER ID
def view_user(userId):
    try:
        user_info = user.view_user_by_id(userId)
        return jsonify(user_info)
    except Exception:
        return 'Usuario no encontrado', 404

@app.route('/users/new',methods=['POST']) #OK CREA USER 
def create_users():
    user_info = request.get_json()
    if 'document' not in user_info:
        return 'El documento de usuario es requerido', 412
    if 'name' not in user_info:
        return 'El nombre de usuario es requerido', 412
    if 'lastName' not in user_info:
        return 'El apellido de usuario es requerido', 412
    if 'phone' not in user_info:
        return 'El telefono de usuario es requerido', 412
    if 'email' not in user_info:
        return 'El email de usuario es requerido', 412
    if 'photoURI' not in user_info:
        return 'La foto es necesaria', 412
    if 'jobPosition' not in user_info:
        return 'El puesto de trabajo de usuario es requerido', 412
    if 'roleId' not in user_info:
        return 'La rol de usuario es requerida', 412
    if 'password' not in user_info:
        return 'La clave es requerida', 412 
    try:
        user.create_user(user_info['document'], user_info['name'], user_info['lastName'], user_info['phone'], user_info['email'], user_info['photoURI'], user_info['password'], user_info['jobPosition'], user_info['roleId'])
        return 'OK', 200
    except Exception:
        return 'El usauario ya existe o no se creo', 412

@app.route('/users/<userId>',methods=['PUT']) #OK ACTUALIZA USER SEGUN ID
def update_user(userId):
    user_info = request.get_json()
    if 'phone' not in user_info:
        return 'El telefono de usuario es requerido', 412
    if 'email' not in user_info:
        return 'El email de usuario es requerido', 412
    if 'photoURI' not in user_info:
        return 'La foto es necesaria', 412
    if 'jobPosition' not in user_info:
        return 'El puesto de trabajo de usuario es requerido', 412
    if 'password' not in user_info:
        return 'La clave  de usuario es requerida', 412
    if 'roleId' not in user_info:
        return 'La rol de usuario es requerida', 412
    if 'status' not in user_info:
        return 'La status de usuario es requerida', 412
    try:
        user.update_user(userId, user_info['phone'], user_info['email'], user_info['photoURI'], user_info['password'], user_info['jobPosition'], user_info['roleId'], user_info['status'])
        return 'OK', 200
    except Exception:
        return 'No se encontro el usuario'
    
@app.route('/tasks/new',methods=['POST'])  #OK CREA TASK
def create_task():
    task_info = request.get_json()
    if 'roleId' not in task_info:
        return 'El campo rol es requerido', 412
    if 'description' not in task_info:
        return 'La descripcion es requerido', 412
    try:
        task.create_task(task_info['roleId'], task_info['description'])
        return 'OK', 200
    except Exception:
        return "No se pudo crear error interno", 404
  
@app.route('/tasks/<taskId>',methods=['GET']) #OK MUESTAR TASK.* y ROLE.* SEGUN TASK ID
def view_task(taskId):
    try:
        task_info = task.view_task(taskId)
        return jsonify(task_info)
    except Exception:
        return "No se encontro la tarea", 404

@app.route('/tasks/role/<roleId>',methods=['GET']) #OK MUESTAR TASKS SEGUN UN ROLE ID
def view_task_by_role(roleId):
    try:
        tasks_info = task.view_task_by_role(roleId)
        return jsonify(tasks_info)
    except Exception:
        return "No se enocntraron tareas", 404

@app.route('/roles/new',methods=['POST'])  #OK CREA ROLE
def create_role():
    role_info=request.get_json()
    if 'description' not in role_info:
        return "La desscripcion del rol es requeria", 412
    if 'access' not in role_info:
        return "La acceso del rol es requeria", 412
    try:
        role.create_role(role_info['description'], role_info['access'])
        return 'OK', 200
    except Exception:
        return "No se pudo crear error interno", 404

@app.route('/roles/<roleId>',methods=['PUT']) #OK ACTUALIZA ROLE
def update_role(roleId):
    role_info=request.get_json()
    if 'description' not in role_info:
        return "La desscripcion del rol es requeria", 412
    if 'access' not in role_info:
        return "La acceso del rol es requeria", 412
    try:
        role.update_role(roleId,role_info['description'], role_info['access'])
        return 'OK', 200
    except Exception:
        return "No se encontro el rol", 404

@app.route('/roles/<roleId>',methods=['GET']) #OK MUESTRA ROLE
def view_role(roleId):
    try:
        role_info=role.view_role(roleId)
        return jsonify(role_info)
    except Exception:
        return 'No se ha encontrado el rol', 404

@app.route('/dialy_records/new',methods=['POST']) #OK CREA REGISTRO
def create_dialyRecord():
    dialyRecord_info=request.get_json()
    if 'sectorId' not in dialyRecord_info:
        return 'El sector es requerido', 412
    if 'roomId' not in dialyRecord_info:
        return 'La habitacion es requerida', 412
    if 'auxNurseId' not in dialyRecord_info:
        return 'Enfermera Requerida', 412 
    if 'nurseId' not in dialyRecord_info:
        return 'Licenciada Requerida', 412
    if 'bed' not in dialyRecord_info:
        return 'Cama requerida', 412
    if 'pacientDocument' not in dialyRecord_info:
        return 'Documento del paciente requerido', 412   
    if 'pacientName' not in dialyRecord_info:
        return 'Nombre del paciente requerido', 412
    if 'pacientLastName' not in dialyRecord_info:
        return 'Apellido del paciente requerido', 412   
    if 'comment' not in dialyRecord_info:
        return 'Comentario requerido', 412     
    try:
        dialyRecord.create_dialyRecord(dialyRecord_info['sectorId'], dialyRecord_info['roomId'], dialyRecord_info['auxNurseId'], dialyRecord_info['nurseId'], dialyRecord_info['bed'], dialyRecord_info['pacientDocument'], dialyRecord_info['pacientName'], dialyRecord_info['pacientLastName'],dialyRecord_info['comment'])
        return 'OK', 200
    except Exception:
        return "No se pudo crear error interno", 404

@app.route('/dialy_records/<recordId>',methods=['GET']) #OK DEVULVE EL REGISTRO Y TODOS SU DATOS RELACIONADOS
def view_dialyRecord(recordId):
    try:
        dialyRecord_info =dialyRecord.view_dialyRecord(recordId)
        return jsonify(dialyRecord_info)
    except Exception:
        return "No se enontro el registro", 404

@app.route('/dialy_records',methods=['GET']) #OK DEVULEVO TODOS LOS REGISTROS REALIZADO; NO JOIN USER 
def view_dialyRecords():
    try:
        dialyRecord_info =dialyRecord.view_dialyRecords()
        return jsonify(dialyRecord_info)
    except Exception:
        return "No se enocntraro registros o ocurrio un error interno", 404

@app.route('/sectors/new',methods=['POST']) #OK CREA UN SECTOR Y SUS ROOMS(VALORES SEPRADOS POR COMA ARRAYS)
def create_sector():
    sector_info=request.get_json()
    if 'name' not in sector_info:
        return 'El sector es requerido', 412
    if 'photoURI' not in sector_info:
        return 'La foto es necesaria', 412
    if 'rooms' not in sector_info:
        return 'La habitacion es requerida', 412
    try:
        sector.create_sector(sector_info['name'], sector_info['photoURI'], sector_info['rooms'] )
        return 'OK', 200
    except Exception:
        return "No se pudo crear error interno", 404

@app.route('/sectors/<sectorId>',methods=['PUT'])  #OK ACTUALIZA UN SECTOR Y ROOMs.NAME VERIFICA QUE NO ESTE CREADO Y LO CREA 
def update_sectors(sectorId):
    sector_info = request.get_json()
    if 'name' not in sector_info:
        return 'El nombre es requerido', 412
    if 'photoURI' not in sector_info:
        return 'La foto es necesaria', 412
    if 'status' not in sector_info:
        return 'El estado es requerido', 412 
    if 'rooms' not in sector_info:
        return 'Las habitaciones son requeridas', 412
    try:
        sector.update_sector(sectorId, sector_info['name'], sector_info['photoURI'], sector_info['status'], sector_info['rooms'],)
        return 'OK', 200
    except Exception:
        return "No se encontro el sector", 404

@app.route('/sectors/<sectorId>',methods=['GET']) #OK DEVULVE LA INFO Y ROOMS DE UN SECTOR
def view_sector(sectorId):
    try:
        sector_info =sector.view_sector(sectorId)
        return jsonify(sector_info)
    except Exception:
        return "No se pudo encontro el secctor", 404

@app.route('/sectors',methods=['GET']) #OK DEVULVE TODOS LOS SECTORES
def view_sectors():
    try:
        sectors_info = sector.view_sectors()
        return jsonify(sectors_info)
    except Exception:
        return "No se oncontraron sectores o ocurrio un error interno", 404
        
@app.route('/sectors/search',methods=['GET']) #OK DEVULEVE EL ID DE UN SECTOR APARTIR DEL NOMBRE
def search_sectorId():
    sector_info=request.get_json()
    try:
        if 'name' not in sector_info:
            return 'El nombre de sector es requerido', 412
        sectorId=sector.search_sectorId_ny_name(sector_info['name'])
        return jsonify(sectorId)
    except Exception:
        return 'No se encontraron sectores con ese nombre', 404

"""
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
