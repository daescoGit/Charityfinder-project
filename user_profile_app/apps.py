from django.apps import AppConfig


class UserProfileAppConfig(AppConfig):
    name = 'user_profile_app'

    def ready(self):
        from . signals import create_user_profile
