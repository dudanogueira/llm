# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_options', '0002_auto_20150708_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightoption',
            name='approved_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flightoption',
            name='rejected_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flightoption',
            name='seen_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flightoption',
            name='sent_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
