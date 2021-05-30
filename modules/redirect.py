# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 


# Import Libraries 
from app import app
from flask import redirect

# Define route "/code".
@app.route('/code')
def code():
  # Makes a redirect to a URL. (For redirect.)
  return redirect('https://github.com/jainamoswal/Flask-Example')
