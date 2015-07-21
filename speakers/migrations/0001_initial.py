# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('document', models.CharField(max_length=100, blank=True)),
                ('contact_phones', models.TextField(blank=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
