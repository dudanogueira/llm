# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20150707_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('route_description', models.TextField(blank=True)),
                ('sent', models.BooleanField(default=False)),
                ('sent_timestamp', models.DateTimeField(blank=True)),
                ('seen', models.BooleanField(default=False)),
                ('seen_timestamp', models.DateTimeField(blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('approved_timestamp', models.DateTimeField(blank=True)),
                ('rejected', models.BooleanField(default=False)),
                ('rejected_timestamp', models.DateTimeField(blank=True)),
                ('rejected_reason', models.TextField(blank=True)),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name=b'Atualizado')),
                ('speaker', models.ForeignKey(to='speakers.Speaker')),
            ],
        ),
    ]
