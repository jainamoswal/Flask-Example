from app import app
from flask import request


@app.route('/q')
def query():
    args = request.args
    return args
