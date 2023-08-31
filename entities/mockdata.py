import json
# from entities.user import User
# from entities.comment import Comment
# from entities.post import Post


# Mock data
users = []
posts = []
comments = []

with open('entities/data.json', 'r') as json_file:
    data = json.load(json_file)
    users, posts, comments = data['users'], data['posts'], data['comments']
    # User.set_id_counter(find_max('id', users))
    # Post.set_id_counter(find_max('id', users))
    # Comment.set_id_counter(find_max('id', users))

# def populate_data(users_, posts_, comments_):
#     find_max = lambda key, itr: max([item[key] for item in itr])
#
#     with open('entities/data.json', 'r') as json_file:
#         data = json.load(json_file)
#         users_, posts_, comments_ = data['users'], data['posts'], data['comments']
#
