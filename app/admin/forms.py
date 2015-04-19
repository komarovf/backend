from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import Required, ValidationError
from werkzeug.security import check_password_hash

from app import db
from app.admin.models import User


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += " ckeditor"
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)
 
 
class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class LoginForm(Form):
    login = TextField(validators=[Required()])
    password = PasswordField(validators=[Required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
            raise ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class AboutForm(Form):
    about = CKTextAreaField()