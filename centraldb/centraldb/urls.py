'''centraldb/urls.py'''
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('centraldb_site.urls')),
]
