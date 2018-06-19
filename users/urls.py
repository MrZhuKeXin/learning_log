'''users的urls'''
from django.urls import re_path
from . import views

app_name='users'

from django.contrib.auth.views import login

urlpatterns=[
    #登陆界面
    re_path(r'^login/$', login, {'template_name':'users/login.html'},name='login'),
    #登出
    re_path(r'^logout/$', views.log_out, name='logout'),
    #注册
    re_path(r'^register/$', views.register, name='register')
]