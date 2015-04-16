from app import adm, db

from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

from app.public.models import Category, SubCategory


class CategoryView(ModelView):
    # Disable model creation
    # can_create = False

    # column_labels = dict(name='Название')
    form_excluded_columns = ('sub_categories')

    def __init__(self, session, **kwargs):
        super(CategoryView, self).__init__(Category, session, **kwargs)


class SubCategoryView(ModelView):
    # Disable model creation
    # can_create = False

    # column_labels = dict(name='Название')
    # form_excluded_columns = ('sub_categories')

    def __init__(self, session, **kwargs):
        super(SubCategoryView, self).__init__(SubCategory, session, **kwargs)


adm.add_view(CategoryView(db.session))
adm.add_view(SubCategoryView(db.session))