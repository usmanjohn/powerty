from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
   
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    path('logout/', views.custom_logout, name='logout'),
    path('profile/<email>', views.view_profile, name = 'profile'),
    path('update-profile/<email>', views.update_profile, name = 'update-profile')
]
