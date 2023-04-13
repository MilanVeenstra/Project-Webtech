from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Posts, Users, Comments
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
    posts = Posts.query.all()
    return render_template("posts.html", title=title, css_route=css_route, user=current_user, posts=posts)

@views.route('/post/<post_id>')
def post_info(post_id):
    css_route = "css/post_info.css"
    post_info = Posts.query.filter_by(post_id=post_id).first()
    title = post_info.post_title
    return render_template("post_info.html", title=title, css_route=css_route, user=current_user, post_info=post_info)

@views.route('/posts/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    title = "Create Post"
    css_route = "css/create_post.css"

    if request.method == 'POST':
        data = {
            'title': request.form.get('title'),
            'post_content': request.form.get('post_content')
        }

        post = PostValidator(data)

        if all(data.values()):
            new_post = Posts(user_id=current_user.id, post_title=post.validate_title(), post_content=data['post_content'])
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('views.home'))
        else:
            flash('title or message cannot be empty!', category='error')


    return render_template("create_post.html", title=title, css_route=css_route, user=current_user)

@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Posts.query.filter_by(post_id=id).first()

    if not post:
        flash("Post does not exists", category='error')
    elif current_user.id != post.user_id:
        flash("You do not have permission", category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted', category='succes')


    return redirect(url_for('views.home'))

@views.route('/profile/<username>')
def profile(username):
    profile_info = Users.query.filter_by(username=username).first()
    profile_posts = Users.posts

    title = profile_info.username.capitalize()
    css_route = "css/profile.css"

    return render_template("profile.html", title=title, css_route=css_route, user=current_user,
                           profile_info=profile_info, profile_posts=profile_posts)


@views.route("/create-comment/<post_id>", methods=['GET', 'POST'])
@login_required
def create_comment(post_id):
    comment = request.form.get('comment')

    if not comment:
        flash('Comment cannot be empty!', category='error')
        return redirect(url_for('views.post_info', post_id=post_id))
    else:
        post = Posts.query.filter_by(post_id=post_id)
        if post:
            comment = Comments(comment_content=comment, user_id=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('views.post_info', post_id=post_id))
        else:
            flash('Post does not exists', category='error')
            return redirect(url_for('views.posts'))


