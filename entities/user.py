from entities.mockdata import users


def find_max(key, items):
    return max([item[key] for item in items])


class User:
    id_counter = 0

    @classmethod
    def set_id_counter(cls, val):
        cls.id_counter = val

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
        cls.set_id_counter(find_max('id', users))
        cls.id_counter = cls.id_counter + 1
        _id = cls.id_counter
        user = User(_id, name)
        users.append(user.to_dict())
        return user.to_dict()
