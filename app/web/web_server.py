from flask import Flask, request, redirect, url_for, session
from flask import render_template
from services import autentication, sector_room, users, dialy_records

app = Flask(__name__)
app.secret_key="OpToSaLuD"

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/error', methods=['GET', 'POST'])
def error():
    return render_template('error.html')

@app.route('/base_template', methods=['GET', 'POST'])
def base_template():
    return render_template('base_template.html')

@app.route('/help', methods=['GET', 'POST'])
def help():
    return render_template('help.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        document =request.form['document']
        password =request.form['password']
        if not autentication.valid_credentials(document, password ):
            error = 'El usuario y/o la contraseña ingresados son incorrectos, contáctese con el supervisor.'
        else:
            sessionInfo = autentication.session_info(document)
            session["user_document"] = document
            session["userId"] = sessionInfo[0]["userId"]
            session["userName"] = sessionInfo[0]["name"]
            session["userLastName"] = sessionInfo[0]["lastName"]
            session["userJobPosition"] = sessionInfo[0]["jobPosition"]
            session["userRoleID" ]= sessionInfo[0]["roleId"]
            session["userRoleDescription"] =sessionInfo[0]["roleDescription"]
            return redirect(url_for('sectors'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/sectors', methods=['GET','POST'])
def sectors():
    userId = session["userId"]
    userName = session["userName"]
    userLastName= session["userLastName"]
    sectors = sector_room.sectors()
    return render_template('sectors.html', userId=userId, userName=userName, userLastName=userLastName, sectors=sectors)

@app.route('/sectors/<sectorId>', methods=['GET','POST'])
def rooms(sectorId):
    userId = session["userId"]
    userName = session["userName"]
    userLastName= session["userLastName"]
    session["sectorId"]=sectorId
    answer = sector_room.rooms(sectorId)
    rooms= answer[0]["rooms"]
    session["sectorName"]=answer[0]["name"]
    sectorName=session["sectorName"]
    return render_template('rooms.html', userId=userId, userName=userName, userLastName=userLastName, rooms=rooms, sectorId=sectorId, sectorName=sectorName)

@app.route('/<sectorId>/<roomId>/tasks', methods=['GET','POST'])
def tasks(sectorId, roomId):
    userId = session["userId"]
    userName = session["userName"]
    userLastName= session["userLastName"]
    sectorName=session["sectorName"]
    session["roomId"]=roomId
    # roomName = sector_room.roomName(sectorId,roomId)
    # session["roomName"]=roomName
    return render_template('tasks.html', userId=userId, userName=userName, userLastName=userLastName, sectorName=sectorName )


@app.route('/reports',methods=['GET','POST'])
def reports():
    userId = session["userId"]
    userName = session["userName"]
    userLastName= session["userLastName"]
    sectorName=session["sectorName"]
    return render_template('reports.html', userId=userId, userName=userName, userLastName=userLastName, sectorName=sectorName)

@app.route('/dialyrecord_new',methods=['GET','POST'])
def dialyrecord_new():
    userId = session["userId"]
    userName = session["userName"]
    userLastName= session["userLastName"]
    sectorId= session["sectorId"]
    roomId=session["roomId"]
    sectorName=session["sectorName"]
    nurses=users.users_by_JobPosition("Nurse")
    if request.method == 'POST':
        nurseId=request.form['nurseId']
        bed=request.form['bed']
        pacientDocument=request.form['pacientDocument']
        pacientName=request.form['pacientName']
        pacientLastName=request.form['pacientLastName']
        comment=request.form['comment']
        dialy_records.newDialyRecord(sectorId, roomId, userId, nurseId, bed, pacientDocument, pacientName, pacientLastName, comment)
    return render_template('dialyrecord_new.html', userId=userId, userName=userName, userLastName=userLastName, sectorId=sectorId, roomId=roomId,sectorName=sectorName, nurses=nurses)

@app.route('/dialyrecords',methods=['GET','POST'])
def dialyrecords():
    userId = session["userId"]
    userName = session["userName"]
    userLastName= session["userLastName"]
    sectorId= session["sectorId"]
    roomId=session["roomId"]
    sectorName=session["sectorName"]
    dialyrecords=dialy_records.dialyrecords()
    return render_template('dialyrecords.html', userId=userId, userName=userName, userLastName=userLastName, sectorName=sectorName, dialyrecords=dialyrecords)

@app.route('/dialyrecords/<recordId>',methods=['GET','POST'])
def dialyrecord(recordId):
    userId = session["userId"]
    userName = session["userName"]
    userLastName= session["userLastName"]
    sectorName=session["sectorName"]
    answer=dialy_records.dialyrecord(recordId)
    record=answer[0]
    return render_template('dialyrecord.html', userId=userId, userName=userName, userLastName=userLastName, sectorName=sectorName, record=record)

@app.route('/users/<userId>',methods=['GET','POST'])
def profile(userId):
    answer=users.userInfo(userId)
    userInfo=answer[0]
    userName = session["userName"]
    userLastName= session["userLastName"]
    return render_template('profile.html',userId=userId, userName=userName, userLastName=userLastName,  user=userInfo )
if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
