from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from pages import views

urlpatterns = [
    path('', views.search_result, name='search_result'),
    path('review/', views.review_list, name='review_list'),
    path('review/new/', views.new, name='new'),
    path('review/<int:id>/', views.show, name='show'),
    path('review/<int:id>/edit/', views.edit, name='edit'),
    path('review/<int:id>/delete/', views.delete, name='delete'),
    path('review/<int:id>/comment/', views.comment, name='comment'),
    path('review/<int:id>/comment/<int:cid>/delete/', views.comment_delete, name="comment_delete"),
    path('review/<int:rid>/rec/', views.review_recommend, name="review_rec"),
    path('review/<int:rid>/comment/<int:cid>/rec/', views.comment_recommend, name="comment_rec"),
    path('get_data/', views.get_data, name='get_data'),
    path('add-gym/', views.add_gym, name='new_gym'),
]
