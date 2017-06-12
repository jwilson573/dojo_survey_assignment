from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "TestKey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    username = session['fullname']
    location = session['location']
    language = session['language']
    comment = session['comment']
    return render_template('results.html', username = username, location = location, language = language, comment = comment)

@app.route('/process', methods=['POST'])
def process():
    session['fullname'] = request.form['name']
    session['location'] = request.form['dojo_loc']
    session['language'] = request.form['fav_lang']
    session['comment'] = request.form['comment']

    return redirect('/results')

app.run(debug=True)