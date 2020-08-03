from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import pages.views

urlpatterns = [
    path('', pages.views.index, name='index'),
    path('review/', pages.views.review, name='review'),
    path('get_data/', pages.views.get_data, name='get_data'),
]
