# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='document_type',
            field=models.CharField(blank=True, max_length=100, choices=[(b'cpf', b'Brazilian CPF'), (b'passport', b'Passport')]),
        ),
        migrations.AddField(
            model_name='speaker',
            name='flight_arranged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='speaker',
            name='origin_city_state',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='require_flight',
            field=models.BooleanField(default=False),
        ),
    ]
