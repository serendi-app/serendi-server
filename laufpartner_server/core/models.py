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

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# from django.db import models
from django.contrib.gis.db import models


class Profile(models.Model):
    '''
    User profile
    '''

    # Special GIS manager
    objects = models.GeoManager()

    # Options for gender
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )

    # Options for fitness level
    LEVEL_BEGINNER = '1'
    LEVEL_INTERMEDIATE = '2'
    LEVEL_ADVANCED = '3'
    LEVEL = (
        (LEVEL_BEGINNER, _('Beginner')),
        (LEVEL_INTERMEDIATE, _('Intermediate')),
        (LEVEL_ADVANCED, _('Advanced')),
    )

    # Age brackets
    AGE_LT18 = '1'
    AGE_18_24 = '2'
    AGE_25_34 = '3'
    AGE_35_44 = '4'
    AGE_45_64 = '5'
    AGE_GT65 = '6'
    AGE = (
        (AGE_LT18, _('Under 18')),
        (AGE_18_24, _('Between 18 and 24')),
        (AGE_25_34, _('Between 25 and 34')),
        (AGE_35_44, _('Between 35 and 44')),
        (AGE_45_64, _('Between 45 and 64')),
        (AGE_GT65, _('More than 65'))
    )

    # Options for training time
    TIME_MORNING = '1'
    TIME_DAY = '2'
    TIME_EVENING = '3'
    TIME_MISC = '4'
    TIME = (
        (TIME_MORNING, _('In the morning')),
        (TIME_DAY, _('During the day')),
        (TIME_EVENING, _('In the evening')),
        (TIME_MISC, _('Differs')),
    )

    user = models.OneToOneField(User,
                                editable=False)
    '''
    The user
    '''

    active = models.BooleanField(verbose_name=_('Active'),
                                 help_text=_('Check if you are actively looking for a partner'),
                                 default=True)
    '''
    Flag indicating whether the user should be included in searches
    '''

    position = models.PointField(geography=True)
    '''
    The user's position
    '''

    gender = models.CharField(verbose_name=_('Gender'),
                              max_length=1,
                              choices=GENDER,
                              default=GENDER_MALE)
    '''
    The user's gender
    '''

    level = models.CharField(verbose_name=_('Your fitness level (approx)'),
                             max_length=1,
                             choices=LEVEL,
                             default=LEVEL_BEGINNER)
    '''
    The user's fitness level
    '''

    age = models.CharField(verbose_name=_('Age'),
                           max_length=1,
                           choices=AGE,
                           default=AGE_18_24)
    '''
    The user's approximate age
    '''

    time = models.CharField(verbose_name=_('Time when you train'),
                            max_length=1,
                            choices=TIME,
                            default=TIME_MORNING)
    '''
    The user's approximate age
    '''
