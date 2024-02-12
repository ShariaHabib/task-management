from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-task/', views.create_task, name='create-task'),
    path('update-task/<int:id>/', views.update_task, name='update-task'),
    path('delete-task/<int:id>/', views.delete_task, name='delete-task'),
    path('logout/', views.logout, name='logout'),
]