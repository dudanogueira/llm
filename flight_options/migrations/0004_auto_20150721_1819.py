# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_options', '0003_auto_20150719_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightoption',
            name='arrival_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flightoption',
            name='departure_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
