from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('charityfinder/', include('charityfinder_app.urls')),
    path('accounts/', include('login_app.urls')),
    # api interface login/out option
    path('api-auth/', include('rest_framework.urls')),
    # all-auth, alt to using custom login app
    # path('accounts/', include('allauth.urls')),
    path('comments/', include('comment_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
