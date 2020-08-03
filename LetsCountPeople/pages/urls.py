from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import pages.views

urlpatterns = [
    path('', pages.views.search_result, name='search_result'),
    path('review/', pages.views.review, name='review'),
    path('review/new/', pages.views.new, name='new'),
    path('review/<int:id>/', pages.views.show, name='show'),
    path('review/<int:id>/update/', pages.views.update, name='update'),
    path('review/<int:id>/delete/', pages.views.delete, name='delete'),
    path('get_data/', pages.views.get_data, name='get_data'),
    path('new_gym/',pages.views.new_gym, name='new_gym'),
]
