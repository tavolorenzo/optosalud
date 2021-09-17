from flask import Flask, request


app = Flask(__name__)

@app.route('/users',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/search',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/{userId}',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/new',methods=['POST'])
def create_users():
    create_users = request.get_json()
    user.create_user(dates_users['document'], dates_users['name'],dates_users['lastname'],dates_users['phone'],dates_users['email'],dates_users['photoURI'],dates_users['password'],dates_users['jobposition'],dates_users['roleId'])
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
