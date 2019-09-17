"""
File-Name: [app]/urls.py
File-Desc: App specific urls
App-Name: las_util_django
Project-Name: Las-Util-Django
Copyright: Copyright (c) 2019, DC Slagel
License-Identifier: BSD-3-Clause
"""

from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #--------------------------------------------#
    # API
    #--------------------------------------------#
    path('api/dump/', views.DumpApi.as_view()),
    path('api/dump', views.DumpApi.as_view()),
    path('api/list/', views.ListApi.as_view()),
    path('api/list', views.ListApi.as_view()),
    re_path('api/detail/(?P<filename>[^/]+)$', views.DetailApi.as_view()),
    #--------------------------------------------#
    # WEB
    #--------------------------------------------#
    path('upload/', views.upload, name='upload'),
    path('list/', views.list, name='list'),
    re_path(r'detail/(?P<docName>[^/]+)$', views.detail, name='detail'),
]
