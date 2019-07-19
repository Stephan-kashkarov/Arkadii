from flask import url_for, redirect, render_template
from app import app

@app.route('/')
def index():
    info = {
        'categories': ["A", "B", "C"]
    }
    return render_template('index.html', info=info)

@app.route('/browse')
def browse():
    return render_template('browse.html')