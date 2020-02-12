from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('edit-profile/', views.editProfile, name='edit-profile'),
    path('change-password/', views.changePassword, name='change-password')
]
