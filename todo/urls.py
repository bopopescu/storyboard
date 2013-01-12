#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Darcy Liu on 2012-03-09.
Copyright (c) 2012 Close To U. All rights reserved.
"""

from django.conf.urls.defaults import *
from todo.views import *


urlpatterns = patterns('todo.views',
            (r'^$',TodoEntryListView.as_view()),
        )