from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
import requests


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # todo authorise read to all
    # todo add author permission/restriction to comment (something with list permissions, lookup)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # todo authorise read to all


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # todo add permissions or remove users view


# another way, function/decorator based
@api_view(['GET'])
def project_detail(request, id):
    url = f"https://api.globalgiving.org/api/public/projectservice/projects/{id}.json?api_key=79638b32-7812-44ef-b361-9eb4ef85aae0"
    api_res = requests.get(url)
    data = api_res.json()
    return Response(data)
    # todo authorise read to all
    # todo protect api key


@api_view(['GET'])
def project_list(request):
    url = f"https://api.globalgiving.org/api/public/projectservice/all/projects/active/ids.json?api_key=79638b32-7812-44ef-b361-9eb4ef85aae0"
    api_res = requests.get(url)
    data = api_res.json()
    return Response(data)
    # todo authorise read to all
    # todo protect api key

# combined charity obj api endpoint? (nested view a thing?)

