from app import app
from flask import request


@app.route('/q')
def query():
    return request.args
