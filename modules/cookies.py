from app import app
from flask import request, make_response

@app.route('/cookies/set')
def set():
    res = make_response({"message":"Cookies set!"})

    res.set_cookie("user", "JKumar", 100)
    res.set_cookie("country", "India", 100)
    res.set_cookie("skill", "hacker", 100)

    return res


@app.route('/cookies/get')
def get():
    cookies = request.cookies
    return cookies


@app.route('/cookies/del')
def clear():
    res = make_response({"message":"Cookies deleted!"})

    res.delete_cookie("user")
    res.delete_cookie("country")
    res.delete_cookie("skill")

    return res
