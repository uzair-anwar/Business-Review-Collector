from django.contrib import admin
from django.urls import path, re_path
from .views import business_endpoint


urlpatterns = [
    path("admin/", admin.site.urls),
    path('<str:business_url>/', business_endpoint, name='business_url'),
]
