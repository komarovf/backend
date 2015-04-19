from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask import redirect, url_for, request, flash
from flask.ext.login import current_user, login_user, logout_user
from flask.ext.admin import Admin, AdminIndexView, BaseView, helpers, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.form.upload import ImageUploadField

from app import app, db, lm
from config import ABOUT_PATH
from app.public.models import Category, SubCategory, Manufacturer, Product, Properties, News, BlogPosts
from app.admin.models import User
from app.admin.forms import LoginForm, AboutForm, CKTextAreaField


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=['GET', 'POST'])
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated():
            return redirect(url_for('.index'))

        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


class CategoryView(ModelView):
    inline_models = [(SubCategory, dict(form_columns=['name', 'id']))]
    form_excluded_columns = ('sub_categories')
    column_list = ('name',)

    def is_accessible(self):
        return current_user.is_authenticated()

    def __init__(self, session, **kwargs):
        super(CategoryView, self).__init__(Category, session, **kwargs)


class ManufacturerView(ModelView):
    # Display map.png for all manuffacturers for first time
    form_excluded_columns = ('location', 'products')
    column_list = ('name', 'url')

    def is_accessible(self):
        return current_user.is_authenticated()

    def __init__(self, session, **kwargs):
        super(ManufacturerView, self).__init__(Manufacturer, session, **kwargs)


class ProductView(ModelView):
	form_overrides = dict(description=CKTextAreaField)
	form_excluded_columns = ('popularity', 'date', 'img_folder')
	column_list = ('name', 'price') 
	inline_models = (Properties,)

	create_template = 'admin/edit.html'
	edit_template = 'admin/edit.html'
	
	def is_accessible(self):
		return current_user.is_authenticated()

	def __init__(self, session, **kwargs):
		super(ProductView, self).__init__(Product, session, **kwargs)


class BlogView(ModelView):
	form_overrides = dict(body=CKTextAreaField)
	form_excluded_columns = ('date',)
	column_list = ('title',)

	create_template = 'admin/edit.html'
	edit_template = 'admin/edit.html'

	def is_accessible(self):
		return current_user.is_authenticated()

	def __init__(self, session, **kwargs):
		super(BlogView, self).__init__(BlogPosts, session, **kwargs)


class NewsView(BlogView):
	def __init__(self, session, **kwargs):
		super(BlogView, self).__init__(News, session, **kwargs)


class AboutView(BaseView):
	@expose('/', methods=['GET', 'POST'])
	def index(self):
		with open(ABOUT_PATH, 'r+') as f:
			about = f.read()
		form = AboutForm()
		if helpers.validate_form_on_submit(form):
			new = form.about.data
			with open(ABOUT_PATH, 'w+') as f:
				f.write(new)
			flash('Success commit!')
		else:
			form.about.data = about
		return self.render('admin/about.html', form=form)


adm = Admin(app, template_mode='bootstrap3', index_view=MyAdminIndexView(), base_template='admin/my_master.html')
adm.add_view(CategoryView(db.session))
adm.add_view(ManufacturerView(db.session))
adm.add_view(ProductView(db.session))
adm.add_view(BlogView(db.session))
adm.add_view(NewsView(db.session))
adm.add_view(AboutView(name='About page'))
