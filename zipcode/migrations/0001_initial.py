# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(max_length=8)),
                ('address', models.CharField(max_length=150)),
                ('neighborhood', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Zipcode',
                'verbose_name_plural': 'Zipcodes',
            },
        ),
    ]
