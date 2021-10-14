from flask import Flask, request, redirect, url_for
from flask import render_template
from services import autentication

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autentication.valid_credentials(request.form['document'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('sector_room'))
    return render_template('login.html', error=error)

@app.route('/sector_room', methods=['GET','POST'])
def sector_room():
    return render_template('sector_room.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
