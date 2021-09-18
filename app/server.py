from app.data.models.user import create_user
from flask import Flask, request
from services.user import user

app = Flask(__name__)

@app.route('/users',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/search',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/{userId}',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/new',methods=['POST'])
def create_users():
    user_info = request.get_json()
    if 'name' not in user_info:
        return 'El nombre de usuario es requerido', 412
    if 'lastName' not in user_info:
        return 'El nombre de usuario es requerido', 412
    if 'password' not in user_info:
        return 'La clave es requerida', 412    
    user.create_user(user_info['document'], user_info['name'], user_info['lastname'], user_info['phone'], user_info['email'], user_info['photoURI'], user_info['password'], user_info['jobposition'], user_info['roleId'])
    return 'OK', 200

@app.route('/tasks/new',methods=['POST'])
#DEFINIR FUCION 

@app.route('/tasks/{taskId}',methods=['PUT'])
#DEFINIR FUCION 

@app.route('/tasks/{taskId}',methods=['GET'])
#DEFINIR FUCION 

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
#DEFINIR FUCION

@app.route('/material_records/{recordId}',methods=['GET'])
#DEFINIR FUCION

@app.route('/material_records',methods=['GET'])
#DEFINIR FUCION

@app.route('/dialy_records/new',methods=['POST'])
#DEFINIR FUCION

@app.route('/dialy_records/{recordId}',methods=['GET'])
#DEFINIR FUCION

@app.route('/dialy_records',methods=['GET'])
#DEFINIR FUCION

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
