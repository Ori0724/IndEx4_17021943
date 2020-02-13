from flask import render_template, Blueprint, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.forms import SignupForm
from app.models import User, city

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html')


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        users = User(username=form.username.data, email=form.email.data)
        try:
            db.session.add(users)
            db.session.commit()
            flash('You are now a registered user!')
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to register {}. Please check your details are correct and resubmit'.format(form.email.data), 'error')
    return render_template('signup.html', form=form)


@bp_main.route('/display', methods=['GET'])
def display():
    display = User.query.all()
    return render_template("display.html", display=display)


@bp_main.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a city to search for")
            return redirect('/')
        results = city.query.filter(city.city.contains(term)).all()
        if not results:
            flash("No cities found with that name.")
            return redirect('/')
        return render_template('search_results.html', results=results)
    else:
        return redirect(url_for('main.index'))
