from django.contrib import admin
from django.urls import path
from .views import business_endpoint


urlpatterns = [
    path("admin/", admin.site.urls),
    path("business/", business_endpoint, name="business")
]
