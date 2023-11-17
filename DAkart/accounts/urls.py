from django.urls import path
from.import views

urlpatterns =[ path('register/', views.register, name='register'),
               path('register/', views.login, name='login') ]