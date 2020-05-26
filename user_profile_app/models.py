from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=25, blank=True)
    # charity org affiliated, (site staff option build in user model)
    verified_affiliated = models.BooleanField(default=False)
    picture = models.ImageField(default='/default_profile.png')

    def __str__(self):
        return self.user.username


class UserOrganization(models.Model):
    pass
