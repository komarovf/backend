from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import app, db
from app.public.models import Category, SubCategory


mod = Blueprint('public', __name__, url_prefix='/public')

@app.route('/')
@mod.route('/')
def home():
	return render_template("public/index.html")

@mod.route('/product')
def product():
	return render_template("public/product.html")

@mod.route('/blog')
def blog():
	return render_template("public/blog.html")

@mod.route('/news')
def news():
	return render_template("public/news.html")

@mod.route('/about')
def about():
	return render_template("public/about.html")

@mod.route('/catalog')
@mod.route('/catalog/<category>')
def catalog(category=None):
	if category is None:
		category = Category.query.first()
	sub_categories = category.sub_categories if category else 'lol'
	return render_template('public/catalog.html', 
							category=category,
							sub_cat=sub_categories)
