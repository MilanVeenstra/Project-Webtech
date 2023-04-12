from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(75))
    username = db.Column(db.String(128), unique=True)

class User_Info(db.Model):
    __tablename__ = 'user_info'
    info_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_image = db.Column(db.String(100))


class Post_Info(db.Model):
    __tablename__ = 'post_info'
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_title = db.Column(db.String(150))
    post_content = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Post_Comment(db.Model):
    __tablename__ = 'post_comment'
    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post_info.post_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    comment_content = db.Column(db.String(10000))







