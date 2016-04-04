# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.liss, name='liss'),
    url(r'^ma$', views.msg, name='msg'),
    url(r'^encc$', views.encc, name='encc'),
    url(r'^dencc$', views.dencc, name='dencc'),
]
