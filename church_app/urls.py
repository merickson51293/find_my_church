from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('church_reg_log', views.church_reg_log),
    path('create_user', views.create_user),
    path('login', views.login),
    path('create_church', views.create_church),
    path('church_login', views.church_login),
    path('church_info', views.church_info),
]