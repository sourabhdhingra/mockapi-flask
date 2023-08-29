from .mockdata import users


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @staticmethod
    def from_dict(dict_obj):
        return User(dict_obj['id'], dict_obj['name'])

    @staticmethod
    def add_user(name):
        _id = len(users) + 1
        user = User(_id, name)
        users.append(user.to_dict())









