from .mockdata import users


class User:
    id_counter = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @classmethod
    def from_dict(cls, dict_obj):
        return User(dict_obj['id'], dict_obj['name'])

    @classmethod
    def add_user(cls, name):
        cls.id_counter = cls.id_counter + 1
        _id = cls.id_counter
        user = User(_id, name)
        users.append(user.to_dict())









