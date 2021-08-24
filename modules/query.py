from app import app
from flask import request


@app.route('/query')
def query():
    args = request.args

    if "name" in args:
        text = f"Welcome {args['name']}"
    else:
        text = "Hi user!"
    return text
