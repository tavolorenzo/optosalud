from flask import Flask, request, redirect, url_for
from flask import render_template
from web.services import rest_api, autentication

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autentication.valid_credentials(request.form['document'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('inicio'))
    return render_template('login.html', error=error)
   
if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
