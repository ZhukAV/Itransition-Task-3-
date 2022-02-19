from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name = 'loginPage'),
    path('register', views.registerPage, name = 'registerPage'),
    path('logout',views.logout, name = "logout"),
    path('main',views.mainPage, name = 'mainPage'),
    path('edit',views.edit, name = 'edit')
]