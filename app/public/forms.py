from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required, Email


class SubscribeForm(Form):
    name = StringField('name', validators=[Required()])
    email = StringField('email', validators=[Required(), Email()])


class SearchForm(Form):
    search = StringField('search', validators=[Required()])
