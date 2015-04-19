import os
import sys
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# inject categories in all templates
from app.public.models import Category
@app.context_processor
def inject_menu():
    return dict(menu=Category.query.all())

from app.public.views import mod as publicModule
from app.admin.views import *
app.register_blueprint(publicModule)


