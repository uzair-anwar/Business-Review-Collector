from django.contrib import admin
from django.urls import path, re_path
from .views import business_endpoint


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^business/(?P<business_name>.+)/$',
            business_endpoint, name='business'),
]
