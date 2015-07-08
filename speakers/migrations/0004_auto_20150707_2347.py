# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0003_auto_20150707_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='name',
            new_name='complete_name',
        ),
        migrations.AddField(
            model_name='speaker',
            name='nickname',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
