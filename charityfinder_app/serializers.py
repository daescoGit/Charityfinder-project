# serializers can exclude fields as well and deserialize
from rest_framework import serializers
from comment_app .models import Comment
from django.contrib.auth import get_user_model
from user_profile_app.models import UserProfile


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(),
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'body', 'created', 'project_id', 'parent',)
        model = Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email',)
        model = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = UserProfile

