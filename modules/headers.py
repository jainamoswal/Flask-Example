from app import app
from flask import request


@app.route('/headers')
def headers():
    header = request.headers
    return "Request headers:<br><br>" + str(header)
