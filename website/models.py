from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(75))
    username = db.Column(db.String(128), unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_image = db.Column(db.Text)
    posts = db.relationship('Posts', backref='users', passive_deletes=True)
    comments = db.relationship('Comments', backref='users', passive_deletes=True)
    likes = db.relationship('Likes', backref='users', passive_deletes=True)

class Posts(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    post_title = db.Column(db.String(150), nullable=False)
    post_content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    comments = db.relationship('Comments', backref='posts', passive_deletes=True)
    likes = db.relationship('Likes', backref='posts', passive_deletes=True)

class Comments(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    comment_content = db.Column(db.Text, nullable=False)

class Likes(db.Model):
    __tablename__ = 'likes'
    like_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id', ondelete="CASCADE"))












