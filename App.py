from flask import Flask, render_template, request

app = Flask(__name__)    # set FLASK_APP=App.py    flask run


@app.route('/')
def hello():
    return render_template('index1.html')

@app.route('/index1.html')
def index():
    return render_template('index1.html')

@app.route('/about.html')
def About():
    return render_template('about.html')


@app.route('/services.html')
def Services():
    return render_template('services.html')


@app.route('/contact.html')
def Contact():
    return render_template('contact.html')






