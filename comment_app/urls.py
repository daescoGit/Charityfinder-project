from django.urls import path
from . import views

app_name = 'comment_app'

urlpatterns = [
    path('projects/<int:pid>/new-comment', views.new_comment, name='new_comment'),
    path('projects/<int:pid>/delete-comment', views.delete_comment, name='delete_comment'),
    path('projects/<int:pid>/new-comment-rating', views.new_comment_rating, name='new_rating'),
]
