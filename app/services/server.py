from flask import Flask, request


app = Flask(__name__)

@app.route('/users',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/search',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/{userId}',methods=['GET'])
#DEFINIR FUCION 

@app.route('/users/new',methods=['POST'])
#DEFINIR FUCION 

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

@app.route('dialy_records',methods=['GET'])
#DEFINIR FUCION

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
