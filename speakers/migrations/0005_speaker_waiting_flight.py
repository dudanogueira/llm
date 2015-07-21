# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_auto_20150707_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='waiting_flight',
            field=models.BooleanField(default=False),
        ),
    ]
