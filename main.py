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


# Comment CRUD operations
@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments)

# Add similar routes for creating, updating, and deleting comments


if __name__ == '__main__':
    app.run(debug=True)
