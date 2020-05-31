from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from comment_app .models import Comment
from .serializers import CommentSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly, IsOwnerOrReadOnly, AllowRead, IsLoggedOrReadOnly
from django.contrib.auth import get_user_model
from django.core.cache import cache
from .gg_api_call import gg_call_project, gg_call_project_list


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsLoggedOrReadOnly,)
    # todo add author permission/restriction to creating comment (list view permission)


class CommentDetail(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowRead,)
    # todo change to admin only view


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# function/decorator based api view
@api_view(['GET'])
@permission_classes((AllowRead,))
def project_detail(request, pid):
    query = 'https://api.globalgiving.org/api/public/projectservice/projects/'
    gg_call_project(pid, query)
    return Response(cache.get(f"project_{pid}"))


@api_view(['GET'])
@permission_classes((AllowRead,))
def project_list(request):
    query = 'https://api.globalgiving.org/api/public/projectservice/all/projects/active/ids'
    gg_call_project_list(query)
    return Response(cache.get('projects'))

