import os


_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

PAGINATION = 3

ADV_PATH = os.path.join(_basedir, 'app', 'templates', 'public', 'adv')
ABOUT_PATH = os.path.join(_basedir, 'app', 'about.txt')

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'This string will be replaced with a proper key in production.'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
DATABASE_CONNECT_OPTIONS = {}

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

WHOOSH_BASE = os.path.join(_basedir, 'search.db')
MAX_SEARCH_RESULTS = 10
