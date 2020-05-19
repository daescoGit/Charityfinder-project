from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Comment(MPTTModel):
    # 8 = deleted user instance
    author = models.ForeignKey(User, on_delete=models.SET(8))
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    project_id = models.IntegerField()
    rated = models.IntegerField(default=0)
    # null = required by MPTT model, protect = comment not deleted, but updated to "deleted" to keep structure
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.author} - {self.created}"


class ProjectTotalRating(models.Model):
    pass


# enable view/api view @auth
# if true / unique or how to limit to 1? some kind of bool?
class UserProjectRating(models.Model):
    pass
