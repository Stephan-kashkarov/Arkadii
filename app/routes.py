from flask import url_for, redirect, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')