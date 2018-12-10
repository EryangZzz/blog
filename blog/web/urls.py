"""__author__ = ErYang"""
from django.conf.urls import url
from web import views

urlpatterns = [
    # 博客首页
    # 127.0.0.1:8000/web/index
    url(r'^index/$', views.index, name='index'),

    url(r'^about/$', views.about, name='about'),

    url(r'^gbook/$', views.gbook, name='gbook'),

    url(r'^info/(\d+)/$', views.info, name='info'),

    url(r'^infopic/$', views.infopic, name='infopic'),

    url(r'^list/$', views.list_art, name='list'),

    url(r'^share/$', views.share, name='share'),

    url(r'^add_art/', views.add_art,name='add_art'),
    url(r'^show_type/(\d+)/', views.show_type, name='show_type')

]
