#!flask/bin/python
import os.path
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
from app.public.models import Category
from app.admin.models import User
from werkzeug.security import generate_password_hash


db.drop_all()
db.create_all()

cat = ['Одяг', 'Взуття', 'Косметика', 'Засоби гігієни', 'Посуд', 'Алкогольні напої',
       'Їжа', 'Чемодани та сумки', 'Товари для дітей', 'Прикраси', 'Побутова хімія', 'Різне']
for i, item in enumerate(cat):
	db.session.add(Category(name=item, css_class=i+1))

user = User()
user.login = 'admin'
user.password = generate_password_hash('admin')
db.session.add(user)

db.session.commit()


if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))