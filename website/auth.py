from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.validation.email_validation import EmailValidator
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = "Login"
    css_route = "css/login.css"

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Loggid in!', category='succes')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again.', category='error')
        else:
            flash('Account does not exists!', category='error')



    return render_template("login.html", title=title, css_route=css_route, user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    title = "Sign-up"
    css_route = "css/sign_up.css"

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        c_password = request.form.get('c_password')

        # v_email = EmailValidator(request.form.get('email'))
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', category='error')
        elif len(email) <4:
            flash('Email is not correct!', category='error')
        elif len(username) < 5:
            flash('Username has to be longer!', category='error')
        elif password != c_password:
            flash('Password don!\'t match', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            # flash('Signed up!', category='succes')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", title=title, css_route=css_route, user=current_user)

