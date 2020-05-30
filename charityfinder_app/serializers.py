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
        fields = '__all__'
        model = UserProfile


class UserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(many=False)

    class Meta:
        fields = ('id', 'username', 'email', 'user_profile',)
        model = get_user_model()

    """def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        
        # nested

        return instance"""
