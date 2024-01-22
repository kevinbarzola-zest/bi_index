from flask import Flask, render_template, redirect, request, url_for, Blueprint


blueprint = Blueprint(
    'authentication_blueprint',
    __name__,
    url_prefix=''
)

pages = ['BI']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', pages=pages)

@app.route('/BI')
def BI():
    return render_template('BI.html')


