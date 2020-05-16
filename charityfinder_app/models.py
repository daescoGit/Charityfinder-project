from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    # any way to avoid null?, 8 = deleted user instance
    author = models.ForeignKey(User, on_delete=models.SET(8))
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    project_id = models.IntegerField()
    up_votes = models.IntegerField(default=0)
    # any way to avoid null?, protect = comment not deleted, but updated to "deleted" to keep structure
    reply_to = models.ForeignKey("self", null=True, on_delete=models.PROTECT, related_name='replies')

    class Meta:
        ordering = ['up_votes', 'created']

    def __str__(self):
        return f"{self.author} - {self.created}"


class ProjectTotalRating(models.Model):
    pass


# enable view/api view @auth
# if true / unique or how to limit to 1?
class UserProjectRating(models.Model):
    pass
