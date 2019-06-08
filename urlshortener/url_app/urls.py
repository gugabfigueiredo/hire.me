# -*- coding: utf-8 -*-

from django.urls import path, re_path, include
from url_app import views
from django.conf.urls.static import static


app_name = 'url_app'

urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    # for our home/index page

    re_path(r'^short/(?P<alias>\w+)$', views.redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL

    re_path(r'^create/$', views.shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL
]

