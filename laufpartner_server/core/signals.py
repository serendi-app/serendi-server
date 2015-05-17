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
from django.db.models.signals import post_save

from laufpartner_server.core.models import Profile


def create_user_profile(sender, instance, created, **kwargs):
    '''
    Every new user gets a profile
    '''
    print('aaaaa')
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
