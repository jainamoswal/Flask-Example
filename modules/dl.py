# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 


# Import Libraries 
from app import app
from flask import send_file

# Define route "/dl".
@app.route("/dl")
def dl_file():
    # Sends defined file. (For download.)
    return send_file('templates/simple.html', as_attachment=True)
