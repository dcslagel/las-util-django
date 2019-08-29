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
    path('upload/', views.upload, name='upload'),
    path('display/', views.display, name='display'),
    re_path(r'^displaydetail/(?P<docName>[^/]+)$', views.displaydetail, name='displaydetail'),
    path('api/versionsection/', views.VersionInfoListCreate.as_view()),
]
