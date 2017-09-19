# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0010_auto_20170917_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='introduction',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='developer',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\xbc\x80\xe5\x8f\x91\xe5\x95\x86', blank=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='score',
            field=models.CharField(default=0, max_length=30, verbose_name=b'\xe8\xaf\x84\xe5\x88\x86'),
        ),
    ]
