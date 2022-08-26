# __init__.py
from flask import Flask
app = Flask(__name__)

UPLOAD_FOLDER = '../static/uploads/'

app.secret_key = "terces"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
DATABASE = "mypets_schema"