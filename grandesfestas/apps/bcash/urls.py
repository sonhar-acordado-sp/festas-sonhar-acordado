# -*- coding: utf-8 -*-
from django.conf.urls import url, include, patterns
from bcash import views

urlpatterns = patterns(
    '',
    url(r'^return_url/', views.BCashUpdateView.as_view(), name='return_url'),
)
