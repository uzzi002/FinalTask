from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),  # Home page with login/register links
    path('register/', views.user_register, name='register'),  # User registration page
    path('login/', views.user_login, name='login'),  # User login page
    path('logout/', views.user_logout, name='logout'),  # User logout action
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard displaying events
    path('create/', views.create_event, name='create_event'),  # Create new event page
    path('edit/<int:pk>/', views.edit_event, name='edit_event'),  # Edit event with given pk
    path('delete/<int:pk>/', views.delete_event, name='delete_event'),  # Delete event with given pk
]
