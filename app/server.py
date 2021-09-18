from app.data.models.user import create_user
from flask import Flask, request
from services.user import user

app = Flask(__name__)

@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users.get_view_user())

@app.route('/users/search',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/{userId}',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/new',methods=['POST'])
if 'name' not in user_info:
        return 'El nombre de usuario es requerido', 412
    if 'lastName' not in user_info:
        return 'El nombre de usuario es requerido', 412
    if 'password' not in user_info:
        return 'La clave es requerida', 412    
    user.create_user(user_info['document'], user_info['name'], user_info['lastname'], user_info['phone'], user_info['email'], user_info['photoURI'], user_info['password'], user_info['jobposition'], user_info['roleId'])
    return 'OK', 200
  

@app.route('/tasks/new',methods=['POST'])
    def create_task():
    task_model = request.get_json()
    if 'roleId' not in user_infotask_model:
        return 'El campo rol es requerido', 412
    if 'title' not in user_info:
        return 'El titulo es requerido', 412
    task.create_task(task_model['roleId'], task_model['title'])
    return 'OK', 200

@app.route('/tasks/{taskId}',methods=['PUT'])
#DEFINIR FUCION 

@app.route('/tasks/{taskId}',methods=['GET'])
 def get_task(taskId):
    try:
        task = autenticacion.get_task(taskId)
        return jsonify(task)
    except Exception:
        return 'Campo rol no encontrado', 404
@app.route('/tasks/{roleId}',methods=['GET'])
#DEFINIR FUCION 

@app.route('/login',methods=['POST'])
#DEFINIR FUCION 

@app.route('/logous',methods=['DELETE'])
#DEFINIR FUCION 

@app.route('/phramac_records/new',methods=['POST'])
#DEFINIR FUCION

@app.route('/pahrmac_records/{recordId}',methods=['GET'])
#DEFINIR FUCION

@app.route('/pahrmac_records',methods=['GET'])
#DEFINIR FUCION

@app.route('/material_records/new',methods=['POST'])

@app.route('/material_records/{recordId}',methods=['GET'])
#DEFINIR FUCION

@app.route('/material_records',methods=['GET'])
#DEFINIR FUCION

@app.route('/dialy_records/new',methods=['POST'])
def create_dialy_record():
if 'sectorId' not in dialy_info:
        return 'El sector es requerido', 412
    if 'roomId' not in dialy_info:
        return 'La habitacion es requerida', 412
    if 'auxNurseId' not in dialy_info:
        return 'Puesto de trabajo requerido', 412 
    if 'nurseId' not in dialy_info:
        return 'Puesto de trabajo requerido', 412
    if 'createdate' not in dialy_info:
        return 'La fecha y hora es requerida', 412  
     if 'bed' not in dialy_info:
        return 'cama requerida', 412
    if 'pacientdocument' not in dialy_info:
        return 'Documento del paciente requerido', 412   
    if 'pacientname' not in dialy_info:
        return 'Nombre del paciente requerido', 412
    if 'pacientlastname' not in dialy_info:
        return 'Apellido del paciente requerido', 412   
     if 'comment' not in dialy_info:
        return 'Comentario requerido', 412        
    dialy.create_dialy_record(dialy_info['sectorId'], dialy_info['roomId'], dialy_info['auxNurseId'], dialy_info['nurseId'], dialy_info['createdate'], user_info['bed'], dialy_info['pacientdocument'], dialy_info['pacientname'], dialy_info['comment'])
    return 'OK', 200


@app.route('/dialy_records/{recordId}',methods=['GET'])
def view_dialyrecord(recordId):
    try:
        dialy =.view_dialyrecord(recordId)
        return jsonify(dialy)
    except Exception:
        return 'Registro no encontrado', 404


@app.route('/dialy_records',methods=['GET'])
def view_dialyrecord():
    return jsonify(.view_dialyrecord())
if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
