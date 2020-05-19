# serializers can exclude fields as well and deserialize
from rest_framework import serializers
from .models import Comment
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')

    class Meta:
        fields = ('id', 'author', 'body', 'created', 'project_id', 'up_votes', 'parent',)
        model = Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username',)
        model = get_user_model()


# rating serializer?
# other?
# full content serializer?
