from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import pages.views

urlpatterns = [
    path('', pages.views.index, name='index'),
    path('review/', pages.views.review, name='review'),
    path('review/new/', pages.views.new, name='new'),
    path('review/<int:id>/', pages.views.show, name='show'),
]