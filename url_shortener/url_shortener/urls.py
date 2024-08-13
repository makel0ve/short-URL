from django.contrib import admin
from django.urls import path, include

from main_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path(r'<str:short_url>', views.redirection),
]
