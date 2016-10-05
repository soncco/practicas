# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from . import views

app_name = 'app'
urlpatterns = [
  
    url(r'^$', views.index, name = 'index'),

]
