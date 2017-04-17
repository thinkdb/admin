#!/bin/env python3
# _*_ coding:utf8 _*_
__Auther__ = 'think'

from django.conf.urls import url
from django.contrib import admin
from cmdb import views
urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^index', views.index, name='index'),

]
