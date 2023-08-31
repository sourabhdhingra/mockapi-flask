from entities.mockdata import comments


def find_max(key, items):
    return max([item[key] for item in items])


class Comment:
    id_counter = 0

    @classmethod
    def set_id_counter(cls, val):
        cls.id_counter = val

    def __init__(self, id, userid, post_id, content):
        self.id = id
        self.userid = userid
        self.post_id = post_id
        self.content = content

    def to_dict(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "post_id": self.post_id,
            "content": self.content,
        }

    @classmethod
    def from_dict(cls, dict_obj):
        return Comment(dict_obj['id'], dict_obj['userid'], dict_obj['post_id'], dict_obj['content'])

    @classmethod
    def add_comment(cls, comment_json):
        cls.set_id_counter(find_max('id', comments))
        cls.id_counter = cls.id_counter + 1
        _id = cls.id_counter
        comment = Comment(_id, comment_json['userid'], comment_json['post_id'], comment_json['content'])
        comments.append(comment.to_dict())
        return comment.to_dict()
