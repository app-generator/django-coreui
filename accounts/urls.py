from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('registration/', views.RegistrationPage, name='daftar'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),

]
