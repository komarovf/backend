import os
import sys
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin


app = Flask(__name__)
app.config.from_object('config')

adm = Admin(app)
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.public.views import mod as publicModule
from app.admin.views import *
app.register_blueprint(publicModule)


