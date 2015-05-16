# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active', help_text='Check if you are actively looking for a partner')),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True, null=True)),
                ('gender', models.CharField(default='m', choices=[('m', 'Male'), ('f', 'Female')], verbose_name='Gender', max_length=1)),
                ('level', models.CharField(default='1', choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced')], verbose_name='Your fitness level (approx)', max_length=1)),
                ('age', models.CharField(default='2', choices=[('1', 'Under 18'), ('2', 'Between 18 and 24'), ('3', 'Between 25 and 34'), ('4', 'Between 35 and 44'), ('5', 'Between 45 and 64'), ('6', 'More than 65')], verbose_name='Age', max_length=1)),
                ('time', models.CharField(default='1', choices=[('1', 'In the morning'), ('2', 'During the day'), ('3', 'In the evening'), ('4', 'Differs')], verbose_name='Time when you train', max_length=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
    ]
