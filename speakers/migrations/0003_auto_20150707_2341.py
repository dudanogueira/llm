# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20150707_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='origin_city_state',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
