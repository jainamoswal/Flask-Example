# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 


# Import Libraries 
import os
import importlib

# Get all files.
views = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".py") and f != "__init__.py"]

# Import all files from modules folder.
for view in views:
    importlib.import_module(os.path.dirname(os.path.realpath(__file__)).split('/')[-1] + "." + view[:-3])
    print('App imported ' + view + ' successfully.')
