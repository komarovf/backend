from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db


mod = Blueprint('public', __name__, url_prefix='/public')

@mod.route('/')
def home():
	return render_template("public/index.html")

@mod.route('/product')
def product():
	return render_template("public/product.html")