# serializers can exclude fields as well and deserialize
from rest_framework import serializers
from comment_app .models import Comment
from django.contrib.auth import get_user_model
from user_profile_app.models import UserProfile
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(),
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'body', 'created', 'project_id', 'parent',)
        model = Comment


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('phone', 'verified_affiliated', 'picture',)
        model = UserProfile


class UserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(many=False)

    class Meta:
        fields = ('id', 'username', 'email', 'user_profile',)
        model = get_user_model()

    def update(self, instance, validated_data):
        nested_serializer = self.fields['user_profile']
        nested_instance = instance.user_profile
        nested_data = validated_data.pop('user_profile')
        nested_serializer.update(nested_instance, nested_data)
        return super(UserSerializer, self).update(instance, validated_data)
