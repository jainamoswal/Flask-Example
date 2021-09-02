from app import app
from flask import request


@app.route('/ip')
def ip():
    if request.headers.getlist("X-Forwarded-For"):
      ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
      ip = request.remote_addr
    return ip
