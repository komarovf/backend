# TODO:
# 1) ADV model
# 2) smart popularity calculation

from app import db


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # relationships
    sub_categories = db.relationship('SubCategory', backref='category', lazy='dynamic')


class SubCategory(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # relationships
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'))
    # products = db.relationship('Products', backref='subcategory', lazy='dynamic')

    def get_manufacturers(self):
        pass

'''
class Manufacturer(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    url = db.Column(db.String(50))
    adress = db.Column(db.String(50))
    phones = db.Column(db.String(50))
    # location
    # relationships
    products = db.relationship('Products', backref='manufacturer', lazy='dynamic')


class Product(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    price = db.Column(db.Float(precision=2))
    properties = db.Column(db.String(200))
    # popularity
    # date
    # img
    # relationships
	subcategory_id = db.Column(db.Integer, db.ForeignKey('sub_category.id', ondelete='CASCADE'))
	manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id', ondelete='CASCADE'))


class News(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	# date
    title = db.Column(db.String(50), unique=True)
    body = db.Column(db.String())


class BlogPosts(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), unique=True)
    body = db.Column(db.String())
    # date


class Subscription(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	# name 
	# mail
'''