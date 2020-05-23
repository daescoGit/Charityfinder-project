from django.urls import path, include
from . import views, api

app_name = 'comment_app'

urlpatterns = [
    path('project/<int:pid>/new-comment', views.new_comment, name='new_comment'),
    path('project/<int:pid>/delete-comment', views.delete_comment, name='delete_comment'),
    path('project/<int:pid>/new-comment-rating', views.new_comment_rating, name='new_rating'),
]
