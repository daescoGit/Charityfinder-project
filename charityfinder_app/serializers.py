# serializers can exclude fields as well and deserialize
from rest_framework import serializers
from .models import Comment
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'author', 'body', 'created', 'project_id', 'reply_to',)
        model = Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username',)
        model = get_user_model()


# rating serializer?
# other?
# full content serializer?
