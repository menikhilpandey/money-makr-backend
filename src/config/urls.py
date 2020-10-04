""" Root URL Configuration for Money Makr Project """

from django.contrib import admin
from django.urls import include, path

from main import urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(main_urls)),
]
