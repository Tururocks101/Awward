from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('projects/', views.projectspage, name='projects'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.registerpage, name='register'),
]
