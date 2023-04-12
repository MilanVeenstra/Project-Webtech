from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Post_Info
from website.validation.post_validation import PostValidator
views = Blueprint('views', __name__)

@views.route('/')
def home():
    title = "Home"
    css_route = "css/home.css"
    return render_template("home.html", title=title, css_route=css_route, user=current_user)

@views.route('/posts', methods=['GET', 'POST'])
def posts():
    title = "Posts"
    css_route = "css/posts.css"
    return render_template("posts.html", title=title, css_route=css_route, user=current_user)

@views.route('/posts/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    title = "Create Post"
    css_route = "css/posts.css"

    if request.method == 'POST':
        data = {
            'title': request.form.get('title'),
            'post_content': request.form.get('post_content')
        }

        post = PostValidator(data)

        if post:
            new_post = Post_Info(user_id=current_user.id, post_title=post.validate_title(), post_content=data['post_content'])
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('views.home'))


    return render_template("create_post.html", title=title, css_route=css_route, user=current_user)