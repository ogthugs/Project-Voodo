# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^login/', 'login.views.login', name='login-page'),
    

