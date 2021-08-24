from app import app
from flask import request


@app.route('/query')
def query():
    args = request.args

    if "showcreds" in args:
        if args['showcreds'] == "true":
            return "user: flask <br>pass: pass"

    if "user" in args:
        user = args['user']
    else:
        return "No username provided."

    if "pass" in args:
        password = args['pass']
    else:
        return "No password provided."

    if user == "flask" and password == "pass":
        text = f"Welcome {user}."
    else:
        text = f"Please provide valid credentials.<br><br>Forgot password get it using /query?showcreds=true"

    return text

