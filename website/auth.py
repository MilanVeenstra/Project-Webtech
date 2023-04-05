from flask import Blueprint, render_template, request, flash
from website.Validation.email_validation import EmailValidator
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = "Login"
    css_route = "css/login.css"

    return render_template("login.html", title=title, css_route=css_route)

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    title = "Sign-up"
    css_route = "css/sign_up.css"

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        c_password = request.form.get('c_password')


        if not EmailValidator.validate_email(email):
            flash('Email is not correct!', category='error')
        elif len(username) < 5:
            flash('Username has to be longer!', category='error')
        elif password != c_password:
            flash('Password don!\'t match', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Signed up!', category='succes')

    return render_template("sign_up.html", title=title, css_route=css_route)
