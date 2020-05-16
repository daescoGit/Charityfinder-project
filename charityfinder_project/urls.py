from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('charityfinder/', include('charityfinder_app.urls')),
    path('accounts/', include('login_app.urls')),
    # api interface login/out option
    path('api-auth/', include('rest_framework.urls')),
    # all-auth, alt to using custom login app
    # path('accounts/', include('allauth.urls')),
]
