from app import app
from flask import request


@app.route('/ip')
def ip():
    return (
        request.headers.getlist("X-Forwarded-For")[0]
        if request.headers.getlist("X-Forwarded-For")
        else request.remote_addr
    )
