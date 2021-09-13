from flask import Flask, request
from servicios.autenticacion import autenticacion

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

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
