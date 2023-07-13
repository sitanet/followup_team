from django.urls import path, include
from . import views





urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerStaff/', views.registerStaff, name='registerStaff'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('staff_profile/', views.staff_profile, name='staff_profile'),
    
    
]