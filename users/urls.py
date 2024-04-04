from django.urls import path
from . import views

app_name = 'users'
urlpattern=[
    path('', views.sign_up, name='sign_up')    
]