from crypt import methods
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key ='cualquier cosa que sea secreta' #Codigo de seguridad, se usa con session/si se cambia y reinicia el servidor los usuarios desloguean

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    languages = request.form['languages']
    comments = request.form['comments']
    print(name)
    session['ninja'] = {
        'name': name,
        'location': location,
        'languages':languages,
        'comments': comments
    }
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)