"""
Configuration File
"""

import os

# grab the folder wehre this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNMAE = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# defin the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)