from django.urls import path
from . import views



urlpatterns = [ 
    path( '', views.posts_list_view , name='posts_list'),
    path( 'create', views.create_post , name='create_post'),
    path( '<int:id>/delete', views.delete_post , name='delete_post'),
    path( '<int:id>/comments', views.create_comment , name='create_comment'),
    path( 'comments/<int:id>/delete', views.delete_comment , name='delete_comment'),
    path( 'comments/<int:id>/delete', views.delete_comment , name='delete_comment'),
] 