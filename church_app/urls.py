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
    path('user_info', views.user_info),
    path('create_church_contact', views.create_church_contact),
    path('create_user_contact', views.create_user_contact),
    path('church_contact', views.church_contact),
    path('user_contact', views.user_contact),
    path('user_church', views.user_church),
    path('create_user_church', views.create_user_church),
    path('user_info_other', views.user_info_other),
    path('finish_user', views.finish_user),
    path('create_church_beliefs', views.create_church_beliefs),
    path('church_beliefs', views.church_beliefs),
    path('church_pastor', views.church_pastor),
    path('create_pastor', views.create_pastor),
    path('create_church_info_other', views.create_church_info_other),
    path('church_info_other', views.church_info_other),
    path('church_success', views.church_success),
    path('church_main', views.church_main),
    path('church_profile/<int:church_id>', views. church_profile),
    path('edit_church/<int:church_id>', views.edit_church),
    path('edit/<int:church_id>', views.edit),
    path('church_add_message', views.church_add_message),
    path('church_add_comment/<int:message_id>', views.church_add_comment),
    path('user_add_comment/<int:message_id>', views.user_add_comment),
    path('delete/<int:message_id>', views.delete),
    path('delete_church/<int:church_id>', views.delete_church),
    path('church_home_page', views.church_home_page),
    path('user_home_page', views.user_home_page),
]