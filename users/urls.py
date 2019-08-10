"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from .import views
from django.urls import path

app_name='users'

urlpatterns = [
    #登陆界面
    url(r'^login/$',LoginView.as_view(template_name='login.html'),name='login'),
    #注销
    url(r'^logout/$',views.logout_view,name='logout'),
    # url(r'^register/$',views.register,name='register'),
]