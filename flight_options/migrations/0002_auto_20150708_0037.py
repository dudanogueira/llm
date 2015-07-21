# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_options', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightoption',
            name='arrival_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='flightoption',
            name='arrival_observations',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='flightoption',
            name='departure_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='flightoption',
            name='departure_observations',
            field=models.TextField(blank=True),
        ),
    ]
