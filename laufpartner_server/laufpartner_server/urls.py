# -*- coding: utf-8 -*-

# This file is part of Laufpartner.
#
# Laufpartner is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Laufpartner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import include, url
from django.contrib import admin

import laufpartner_server.core.api.views as api_core_views

### /api/v2 - django rest framework
router = routers.DefaultRouter()
router.register(r'core', api_core_views.search, base_name='core')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/search$', api_core_views.search),
]

urlpatterns = format_suffix_patterns(urlpatterns)