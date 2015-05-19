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

from django.contrib.gis.measure import Distance

from rest_framework.decorators import api_view
from rest_framework.response import Response

from laufpartner_server.core.api.serializers import SearchSerializer
from laufpartner_server.core.models import Profile


@api_view()
def search(request):
    """
    Perform a search
    """
    serializer = SearchSerializer(data=request.query_params)
    serializer.is_valid()

    # All is well, perform a search, sort and rank
    if serializer.is_valid():
        out = []
        p = Profile.objects.filter(active=True,
                                   position__dwithin=(request.user.profile.position,
                                                      Distance(km=serializer.data['radius'])))\
                           .exclude(user=request.user)\
                           .distance(request.user.profile.position)\
                           .order_by('distance')
        for profile in p:
            out.append({'user': profile.user.username,
                        'distance': profile.distance.m})
        return Response(out)
    else:
        return Response(serializer.errors)
