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

from rest_framework import serializers

from laufpartner_server.core.models import Profile


class SearchSerializer(serializers.Serializer):
    '''
    Serializes the parameters needed to perform a search
    '''

    radius = serializers.IntegerField(required=True,
                                      max_value=30)
    '''
    Radius to search users in
    '''

    gender = serializers.MultipleChoiceField(required=True,
                                             choices=Profile.GENDER)
    '''
    Users gender to match
    '''

    level = serializers.MultipleChoiceField(required=True,
                                            choices=Profile.LEVEL)
    '''
    Users fitness level to match
    '''

    age = serializers.MultipleChoiceField(required=True,
                                          choices=Profile.AGE)
    '''
    Users age bracket to match
    '''

    time = serializers.MultipleChoiceField(required=True,
                                           choices=Profile.TIME)
    '''
    Users time for running to match
    '''
