from django.urls import path
from .import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('plants/', views.plants, name='plants'),
    path('register/', views.register, name="Sign Up"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # path("addPlants/", views.addPlants, name="addPlants")
]