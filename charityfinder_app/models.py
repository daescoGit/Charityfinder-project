from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class UserProjectRating(models.Model):
    project_id = models.IntegerField(db_index=True)
    user = models.ForeignKey(User, on_delete=models.SET(8))
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])


def project_calculated_rating(pid):
    project_list = UserProjectRating.objects.filter(project_id=pid)
    avg = project_list.aggregate(Avg('rating'))['rating__avg']
    return avg
