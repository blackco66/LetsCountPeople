from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import pages.views

urlpatterns = [
    path('', pages.views.search_result, name='search_result'),
    path('', pages.views.index, name='index'),
    path('review/', pages.views.review, name='review'),
]
