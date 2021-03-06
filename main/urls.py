from django.urls import path, re_path
from . import views
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('', views.loginPage, name = 'loginPage'),
    path('register', views.registerPage, name = 'registerPage'),
    path('logout',views.logout, name = "logout"),
    path('main',views.mainPage, name = 'mainPage'),
    path('edit',views.edit, name = 'edit'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]