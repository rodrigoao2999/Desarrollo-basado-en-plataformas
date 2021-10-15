import re
from flask import Flask , render_template , request , redirect , url_for , session

app = Flask(__name__ , template_folder='template')
app.secret_key="hola123"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=["POST"])
def login():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        session['user'] = email
        return redirect(url_for('cv'))
    else:
        return "bad request"

@app.route('/cv')
def cv():
    if 'user' in session:
        return render_template('cv.html')
    else:
        return "NO TIENE PERMISO PARA ACCEDER AL CV"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)