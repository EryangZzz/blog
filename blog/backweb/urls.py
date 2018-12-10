"""__author__ = ErYang"""
from django.conf.urls import url
from backweb import views

urlpatterns = [
    # 登录页面
    url(r'^login/', views.login, name='login'),
    # 管理后台主页
    url(r'^index/', views.index, name='index'),
    # 注册页面
    url(r'^register/', views.register, name='register'),
    # 注销账号
    url(r'^logout/', views.logout, name='logout'),
    # 文章页面
    url(r'^article/', views.article, name='article'),
    # 删除文章
    url(r'^del_article/(\d+)/', views.del_article, name='del_article'),
    # 增加文章
    url(r'^add_article/', views.add_article, name='add_article'),
    # 修改文章
    url(r'^edit_article/(\d+)/', views.edit_article, name='edit_article'),
    # 展示文章
    url(r'^show_article/(\d+)/', views.show_article, name='show_article'),
    # 登录日志
    url(r'^loginlog/', views.loginlog, name='loginlog'),
]

