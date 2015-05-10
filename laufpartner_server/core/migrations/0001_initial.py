# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, help_text='Check if you are actively looking for a partner', verbose_name='Active')),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True)),
                ('gender', models.CharField(default=b'm', max_length=1, verbose_name='Gender', choices=[(b'm', 'Male'), (b'f', 'Female')])),
                ('level', models.CharField(default=b'1', max_length=1, verbose_name='Your fitness level (approx)', choices=[(b'1', 'Beginner'), (b'2', 'Intermediate'), (b'3', 'Advanced')])),
                ('age', models.CharField(default=b'2', max_length=1, verbose_name='Age', choices=[(b'1', 'Under 18'), (b'2', 'Between 18 and 24'), (b'3', 'Between 25 and 34'), (b'4', 'Between 35 and 44'), (b'5', 'Between 45 and 64'), (b'6', 'More than 65')])),
                ('time', models.CharField(default=b'1', max_length=1, verbose_name='Time when you train', choices=[(b'1', 'In the morning'), (b'2', 'During the day'), (b'3', 'In the evening'), (b'4', 'Differs')])),
                ('user', models.OneToOneField(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
