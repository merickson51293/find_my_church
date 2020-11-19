from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('church_reg_log', views.church_reg_log),
    path('create_user', views.create_user),
    path('login', views.login),
    path('create_church', views.create_church),
    path('church_login', views.church_login),
    path('logout', views.logout),
    path('church_info', views.church_info),
    path('create_church_contact', views.create_church_contact),
    path('church_contact', views.church_contact),
    path('create_church_beliefs', views.create_church_beliefs),
    path('church_beliefs', views.church_beliefs),
    path('church_pastor', views.church_pastor),
    path('create_pastor', views.create_pastor),
    path('create_church_info_other', views.create_church_info_other),
    path('church_info_other', views.church_info_other),
    path('church_success', views.church_success),
    path('church_main', views.church_main),
    path('church_profile', views. church_profile),
    path('add_message', views.add_message),
    path('delete/<int:message_id>', views.delete),
    path('delete_church/<int:church_id>', views.delete_church),
    path('home_page', views.home_page),
]