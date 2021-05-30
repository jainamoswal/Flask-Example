# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 


# Import Libraries 
from flask import Flask

# Define app.
app = Flask(__name__)

# Import the __init__.py from modules which had imported all files from the folder.
import modules
