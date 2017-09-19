# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0009_file_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='unique_name',
            field=models.CharField(max_length=30, null=True, verbose_name=b'name', blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='unique_name',
            field=models.CharField(max_length=30, null=True, verbose_name=b'name', blank=True),
        ),
    ]
