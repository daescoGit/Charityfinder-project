from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
# pluralize used to add 's' when appropriate
from django.template.defaultfilters import pluralize
from datetime import timedelta
from django.utils import timezone


class Comment(MPTTModel):
    # 8 = deleted user instance
    author = models.ForeignKey(User, on_delete=models.SET(8))
    body = models.TextField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    project_id = models.IntegerField()
    rated = models.ManyToManyField(User, through='UserCommentRating', related_name='rated_user')
    # null = required by MPTT model, comment not deleted, but updated to "deleted" to keep structure
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.author} - {self.created}"

    def comment_age(self):
        age = timezone.now() - self.created
        if age < timedelta(minutes=1):
            return f'{age.seconds} second{pluralize(age.seconds)} ago'
        elif age < timedelta(hours=1):
            # only tracks seconds
            # total_seconds returns a float
            minutes = int(age.total_seconds()) // 60
            return f'{minutes} minute{pluralize(minutes)} ago'
        elif age < timedelta(days=1):
            hours = int(age.total_seconds()) // 3600
            return f'{hours} hour{pluralize(hours)} ago'
        else:
            return f'{age.days} day{pluralize(age.days)} ago'

# a user can up OR down vote a/many comments ONCE
# a comment can be up OR down voted by a/many users
# a comment have an int rating
# double/tri unique pk?, insert or update, check if exist ..


class UserCommentRating(models.Model):
    # comment not deleted, but updated to "deleted" to keep structure
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # 8 = deleted user instance
    user = models.ForeignKey(User, on_delete=models.SET(8))
    state = models.TextField()


class ProjectTotalRating(models.Model):
    pass


# enable view/api view @auth
# if true / unique or how to limit to 1? some kind of bool?
class UserProjectRating(models.Model):
    pass



