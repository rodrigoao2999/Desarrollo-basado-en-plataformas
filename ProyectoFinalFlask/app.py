
from flask import Flask , render_template , request , redirect , url_for , session


app = Flask(__name__ , template_folder='template')
app.secret_key="abcd1234"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        session['user'] = email
        return redirect(url_for('eleccion'))
    else:
        return "bad request"

@app.route('/eleccion')
def eleccion():
    if 'user' in session:
        return render_template('eleccion.html')
    else:
        return "NO TIENE PERMISO PARA ACCEDER AL CV"

@app.route('/cv')
def cv():
     return render_template('cv.html')
 
 
@app.route('/cv2')
def cv2():
     return render_template('secondCv.html')



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)