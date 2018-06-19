from django.urls import re_path
from . import views

app_name='learning_logs'

urlpatterns=[
    #主页
    re_path(r'^$', views.index, name='index'),

    #显示所有主题
    re_path(r'^topics/$', views.topics, name='topics'),

    #显示特定主题的页面
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #添加新主题
    re_path(r'^new_topic$', views.new_topic, name='new_topic'),

    #添加某个主题下的条目
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),

    #用于编辑某项条目的请求
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]