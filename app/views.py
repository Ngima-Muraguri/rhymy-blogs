from flask import render_template
from .app import app


@app.route('/')
def index():
    love='milcah'
    return render_template('index.html', love=love)
