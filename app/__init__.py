import os
import sys
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.admin import Admin
from flask.ext.babel import Babel


app = Flask(__name__)
app.config.from_object('config')

babel = Babel(app)
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

# Admin page initialize
adm = Admin(app, template_mode='bootstrap3', index_view=MyAdminIndexView(), base_template='admin/my_master.html')
adm.add_view(CategoryView(db.session))
adm.add_view(ManufacturerView(db.session))
adm.add_view(ProductView(db.session))
adm.add_view(BlogView(db.session))
adm.add_view(NewsView(db.session))
adm.add_view(AboutView(name='About page'))
