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
    body = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # indexed for faster queries on individual project endpoints
    project_id = models.IntegerField(db_index=True)
    rated = models.ManyToManyField(User, through='UserCommentRating', related_name='rated_user')
    # null = required by MPTT model, comment not deleted, but updated to "deleted" to keep structure
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.author} - {self.created}"

    def comment_age(self):
        age = timezone.now() - self.created
        if age < timedelta(minutes=1):
            return f"{age.seconds} second{pluralize(age.seconds)} ago"
        elif age < timedelta(hours=1):
            # only tracks seconds
            # total_seconds returns a float
            minutes = int(age.total_seconds()) // 60
            return f"{minutes} minute{pluralize(minutes)} ago"
        elif age < timedelta(days=1):
            hours = int(age.total_seconds()) // 3600
            return f"{hours} hour{pluralize(hours)} ago"
        else:
            return f"{age.days} day{pluralize(age.days)} ago"

    def comment_calculated_rating(self):
        ups = UserCommentRating.objects.filter(comment=self.pk, state='1').count()
        downs = UserCommentRating.objects.filter(comment=self.pk, state='-1').count()
        return ups - downs


class UserCommentRating(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET(8))
    state = models.CharField(max_length=2)
