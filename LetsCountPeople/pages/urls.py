from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import pages.views

urlpatterns = [
    path('', pages.views.search_result, name='search_result'),
    path('review/', pages.views.review, name='review'),
    path('review/new/', pages.views.new, name='new'),
    path('review/<int:id>/', pages.views.show, name='show'),
    path('review/<int:id>/edit/', pages.views.edit, name='edit'),
    path('review/<int:id>/delete/', pages.views.delete, name='delete'),
    path('review/<int:id>/comment/', pages.views.comment, name='comment'),
    # path('review/<int:id>/comment/<int:cid>/', pages.views.comment_update, name="comment_update"),
    path('review/<int:id>/comment/<int:cid>/delete/', pages.views.comment_delete, name="comment_delete"),
    path('get_data/', pages.views.get_data, name='get_data'),
    path('add-gym/',pages.views.add_gym, name='new_gym'),
]
