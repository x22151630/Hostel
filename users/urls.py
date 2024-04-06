from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'users'

urlpatterns=[
   
    path('signin/', auth_views.LoginView.as_view(), name='sign_in'),
]