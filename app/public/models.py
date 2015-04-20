# TODO:
# 1) ADV model
# 2) smart popularity calculation

from random import randint
from datetime import datetime
from app import db


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    css_class = db.Column(db.Integer(), unique=True, nullable=False)
    sub_categories = db.relationship('SubCategory', backref='category', lazy='dynamic')

    def total_products(self):
        total = 0
        for sub in self.sub_categories:
            total += sub.products.count()
        return total

    def __repr__(self):
        return str(self.name)


class SubCategory(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id', ondelete='CASCADE'))
    products = db.relationship('Product', backref='subcategory', lazy='dynamic')

    def __repr__(self):
        return str(self.name)


class Manufacturer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    url = db.Column(db.String(50))
    adress = db.Column(db.String(50), nullable=False)
    phones = db.Column(db.Text(), nullable=False)
    location = db.Column(db.String(50))
    # logo = db.Column(db.String(50))
    products = db.relationship('Product', backref='manufacturer', lazy='dynamic')

    def __repr__(self):
        return str(self.name)


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    # atrr for sorting products
    popularity = db.Column(db.Integer())
    date = db.Column(db.DateTime())
    # own image folder for every product
    img_folder = db.Column(db.String(50))
    subcategory_id = db.Column(db.Integer(), db.ForeignKey('sub_category.id', ondelete='CASCADE'), nullable=False)
    manufacturer_id = db.Column(db.Integer(), db.ForeignKey('manufacturer.id', ondelete='CASCADE'), nullable=False)
    properties = db.relationship('Properties', backref='product', lazy='dynamic')

    def __init__(self):
        # Random number for product popularity :)
        self.popularity = (lambda: randint(1, 10))()
        self.date = datetime.utcnow()


class Properties(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(50))
    value = db.Column(db.String(25), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id', ondelete='CASCADE'))

    def __repr__(self):
        return str(self.name)


class News(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime())
    title = db.Column(db.String(50), unique=True, nullable=False)
    body = db.Column(db.Text(), nullable=False)

    def __init__(self):
        self.date = datetime.utcnow()


class BlogPosts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime())
    title = db.Column(db.String(50), unique=True, nullable=False)
    body = db.Column(db.Text(), nullable=False)

    def __init__(self):
        self.date = datetime.utcnow()


class Subscription(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
