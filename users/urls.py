from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('account_info/', views.account_info, name='account_info'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
]