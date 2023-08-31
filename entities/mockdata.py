import json

# Mock data
users = []
posts = []
comments = []

with open('entities/data.json', 'r') as json_file:
    data = json.load(json_file)
    users, posts, comments = data['users'], data['posts'], data['comments']