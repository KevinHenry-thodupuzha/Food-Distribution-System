from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_feed, name='public_feed'),
    path('dashboard/', views.user_feed, name='user_feed'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('my-interests/', views.my_interests, name='my_interests'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
