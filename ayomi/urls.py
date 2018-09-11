"""ayomi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ayomi import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.main),

    url(r'^logout/', views.logout_view, name="logout"),
    url(r'^login/', views.do_login, name="login"),
    url(r'^accounts/login/', views.login_view, name="login_view"),

    url(r'^main/', views.main, name="main_view"),
    url(r'^change_email/(?P<email>[a-zA-Z0-9\.\ ]+\@[a-zA-Z0-9\.]+)/$', views.modify_email, name="mail_modify"),
    url(r'^change_first_name/(?P<first_name>[a-zA-Z0-9\ ]+)/$', views.modify_first_name, name="first_name_modify"),
    url(r'^change_last_name/(?P<last_name>[a-zA-Z0-9\ ]+)/$', views.modify_last_name, name="last_name_modify"),
]
