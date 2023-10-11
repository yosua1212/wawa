from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['UPLOAD_FOLDER'] = 'app/static'  # Gantilah dengan lokasi penyimpanan yang sesuai
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes
