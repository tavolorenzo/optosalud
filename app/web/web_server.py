from flask import Flask, request, redirect, url_for
from flask import render_template
from services import autentication

app = Flask(__name__)

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
        if not autentication.valid_credentials(request.form['document'], request.form['password']):
            error = 'El usuario y/o la contraseña ingresados son incorrectos, contáctese con el supervisor.'
        else:
            return redirect(url_for('sector_room'))
    return render_template('login.html', error=error)

@app.route('/sector_room', methods=['GET','POST'])
def sector_room():
    return render_template('sector_room.html')

@app.route('/task',methods=['GET','POST'])
def task():
    return render_template('task_aux.html')

@app.route('/reports',methods=['GET','POST'])
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
