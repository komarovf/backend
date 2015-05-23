from os import listdir
from os.path import isfile, join
from random import sample

from flask import Blueprint, request, render_template, abort, url_for, redirect, flash, g

from app import app, db
from config import PAGINATION, ADV_PATH, ABOUT_PATH, MAX_SEARCH_RESULTS
from app.public.models import Category, SubCategory, Product, Manufacturer, BlogPosts, News, Subscription
from app.public.forms import SubscribeForm, SearchForm


mod = Blueprint('public', __name__)


@app.before_request
def before_request():
    g.search_form = SearchForm()


@mod.route('/search', methods=['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('public.home'))
    return redirect(url_for('public.search_results', query=g.search_form.search.data))


@mod.route('/search_results/<query>')
def search_results(query):
    results = []#Product.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    return render_template('public/search_results.html',
                           title='Результати пошуку',
                           query=query,
                           results=results)


@mod.route('/', methods=['GET', 'POST'])
def home():
    '''Index view'''

    # Choose six random type2_*.html advs from templates/public/adv
    try:
        adv = sample([f for f in listdir(ADV_PATH) if isfile(join(ADV_PATH, f)) and f.startswith('type2')], 6)
    except:
        adv = []
    news = News.query.order_by(News.date).limit(4)

    # subscription
    form = SubscribeForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        db.session.add(Subscription(name=name, mail=email))
        db.session.commit()
        flash('Ви успішно підписались на розсилку, {}!'.format(name))
        return redirect(url_for('public.home'))

    return render_template("public/index.html",
                           title='Купуй українське',
                           adv=adv,
                           news=news,
                           form=form)


@mod.route('/<cat>')
@mod.route('/<cat>/<int:id>')
@mod.route('/<cat>/<page>')
def post(id=None, page='p1', cat=''):
    '''Blog and news view'''
    model = None
    try:
        page = int(page[1:])
    except:
        abort(404)

    if cat == 'news':
        model = News
        title = 'Новини'
    elif cat == 'blog':
        model = BlogPosts
        title = 'Блог'
    else:
        abort(404)

    template = "public/post.html" if id else "public/posts.html"

    if id is None:
        posts = model.query.paginate(1, page * PAGINATION, False)
        for p in posts.items:
            p.body = p.body[:100] + '...' if len(p.body) > 100 else p.body
    else:
        posts = model.query.get_or_404(id)

    return render_template(template,
                           title=title,
                           posts=posts,
                           cat=cat)


@mod.route('/about')
def about():
    '''About page view'''
    with open(ABOUT_PATH, 'r+') as f:
        text = f.read()
    return render_template("public/about.html",
                           title='Про нас',
                           text=text)


@mod.route('/catalog')
@mod.route('/catalog/<int:category_id>')
@mod.route('/catalog/<int:category_id>/<page>')
@mod.route('/catalog/<int:category_id>/<int:sub_id>')
@mod.route('/catalog/<int:category_id>/<int:sub_id>/<page>')
@mod.route('/catalog/<int:category_id>/<int:sub_id>/<int:product_id>')
def catalog(category_id=1, sub_id=None, product_id=None, page='p1'):
    '''Catalog view, includes category, subcategory and product view'''

    # need for navigation links
    nav = 1

    title = 'Каталог'
    product_count = 0
    sub_cat = None
    manufacturers = None
    products = None
    category = Category.query.get_or_404(category_id)
    try:
        page = int(page[1:])
    except:
        abort(404)

    template = 'public/product.html' if product_id else 'public/catalog.html'

    if sub_id and product_id is None:
        # set variables for SubCategory-catalog view
        nav = 2
        sub_cat = SubCategory.query.get_or_404(sub_id)
        products = sub_cat.products.paginate(1, page * PAGINATION, False)
        product_count = sub_cat.products.count()
        manufacturers = list({p.manufacturer for p in sub_cat.products})
    elif product_id:
        # set variables for Product view
        nav = 3
        products = Product.query.get_or_404(product_id)
        manufacturers = products.manufacturer
        sub_cat = SubCategory.query.get(products.subcategory_id)
        title = products.name
    else:
        # set variables for Category-catalog view
        products = Product.query.filter(Product.subcategory_id.in_(map(lambda x: x.id, category.sub_categories))).paginate(1, page * PAGINATION, False)
        product_count = sum(sub.products.count() for sub in category.sub_categories)
        manufacturers = set()
        for sub in category.sub_categories:
            for p in sub.products:
                manufacturers.add(p.manufacturer)

    # Choose two random type1_*.html advs from templates/public/adv
    try:
        adv = sample([f for f in listdir(ADV_PATH) if isfile(join(ADV_PATH, f)) and f.startswith('type1')], 2)
    except:
        adv = []

    return render_template(template,
                           adv=adv,
                           title=title,
                           nav=nav,
                           count=product_count,
                           category=category,
                           sub=sub_cat,
                           products=products,
                           manufacturers=manufacturers)
