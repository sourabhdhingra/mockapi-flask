from .mockdata import posts


class Post:
    id_counter = 0

    def __init__(self, id, userid, title, content):
        self.id = id
        self.userid = userid
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            'id': self.id,
            'userid': self.userid,
            'title': self.title,
            'content': self.content
        }

    @classmethod
    def add_post(cls, post_json):
        cls.id_counter = cls.id_counter + 1
        _id = cls.id_counter
        print(_id, post_json['userid'], post_json['title'], post_json['content'])
        post = Post(_id, post_json['userid'], post_json['title'], post_json['content'])
        posts.append(post.to_dict())
