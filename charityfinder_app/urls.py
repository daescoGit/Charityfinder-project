from django.urls import path, include
from .api import CommentList, CommentDetail, UserList, UserDetail
from . import views, api

app_name = 'charityfinder_app'

urlpatterns = [
    path('', views.index, name='index'),
    # all-auth, alt to using custom login app
    # path('accounts/', include('allauth.urls')),
    path('project/<int:id>/', views.project_detail_view),

    # API
    path('api/v1/comments/', CommentList.as_view()),
    path('api/v1/comments/<int:pk>/', CommentDetail.as_view()),
    path('api/v1/users/', UserList.as_view()),
    path('api/v1/users/<int:pk>/', UserDetail.as_view()),
    path('api/v1/projects/<int:id>/', api.project_detail),
    path('api/v1/projects/', api.project_list),
    # api interface login/out option
    path('api/v1/api-auth', include('rest_framework.urls')),
    # django-rest-auth provided endpoints, integrated token handling, validation etc.
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/signup', include('rest_auth.registration.urls')),
]
