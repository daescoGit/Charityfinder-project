from django.urls import path, include
from .api import CommentList, CommentDetail, UserList, UserDetail
from . import views, api

app_name = 'charityfinder_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pid>/', views.project_detail_view, name='project'),
    path('project/<int:pid>/new-comment', views.new_comment_view, name='new_comment'),

    # API
    path('api/v1/comments/', CommentList.as_view()),
    path('api/v1/comments/<int:pk>/', CommentDetail.as_view()),
    path('api/v1/users/', UserList.as_view()),
    path('api/v1/users/<int:pk>/', UserDetail.as_view()),
    path('api/v1/projects/<int:id>/', api.project_detail),
    path('api/v1/projects/', api.project_list),
    # django-rest-auth provided endpoints, integrated token handling, validation etc.
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/signup/', include('rest_auth.registration.urls')),
]
