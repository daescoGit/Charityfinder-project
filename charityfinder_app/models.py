from django.db import models
from django.contrib.auth.models import User


def get_sentinel_user():
    return User().objects.get_or_create(username='User deleted')[0]


def get_sentinel_comment():
    return Comment().objects.get_or_create(body='Comment deleted')[0]


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    project_id = models.IntegerField()  # should be textfield if comparable

    def __str__(self):
        return f"{self.author} - {self.created_at}"


# alt, field in comment (extra null issue) - reply to self fk default?
class ReplyComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    project_id = models.IntegerField()
    reply_to = models.ForeignKey(Comment, on_delete=models.SET(get_sentinel_comment))

    def __str__(self):
        return f"{self.author} - {self.created_at}"
# rating? (user / all)
#
