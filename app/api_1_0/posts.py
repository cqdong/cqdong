from . import api
from flask import request, g, jsonify
from ..models import Post
from .. import db

@api.route('/posts/', methods=['POST'])
def new_post():
    post = Post.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())

@api.route('/posts/')
def get_post():
    posts = Post.query.all()
    return jsonify({ 'posts': [post.to_json() for post in posts] })
