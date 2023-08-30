from flask import Flask, request, jsonify
from entities import user
from entities.mockdata import users, posts, comments
from entities.user import User
from entities.post import Post
from entities.comment import Comment

app = Flask(__name__)


# User CRUD operations
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    return jsonify(user) if user else ('User not found', 404)


@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    User.add_user(new_user['name'])
    return jsonify(new_user), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return 'User not found', 404
    user.update(request.json)
    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return 'User not found', 404
    users.remove(user)
    return '', 204


# Post CRUD operations
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)


# Add similar routes for creating, updating, and deleting posts
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.json
    user = next((user for user in users if user['id'] == new_post['userid']), None)
    if not user:
        return 'User not found', 404
    Post.add_post(new_post)
    return jsonify(new_post), 201


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    return jsonify(post) if post else ('Post not found', 404)


@app.route('/posts/<int:post_id>', methods=['POST'])
def update_post(post_id):
    new_post = request.json
    post = next((post for post in posts if post['id'] == post_id), None)
    if not post:
        return 'Post not found', 404
    if post['userid'] != new_post['userid']:
        return 'Invalid userid', 400
    user = next((user for user in users if user['id'] == new_post['userid']), None)
    if not user:
        return 'User not found', 404
    post.update(request.json)
    return jsonify(post)


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if not post:
        return 'Post not found', 404
    posts.remove(post)
    return '', 204


# Comment CRUD operations
@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments)


# Add similar routes for creating, updating, and deleting comments
@app.route('/comments', methods=['POST'])
def create_comment():
    new_comment = request.json
    user = next((user for user in users if user['id'] == new_comment['userid']), None)
    if not user:
        return 'User not found', 404
    post = next((post for post in posts if post['id'] == new_comment['post_id']), None)
    if not post:
        return 'Post not found', 404
    Comment.add_comment(new_comment)
    return jsonify(request.json)


if __name__ == '__main__':
    app.run(debug=True)
