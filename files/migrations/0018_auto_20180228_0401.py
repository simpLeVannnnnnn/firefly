# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0017_auto_20180228_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='introduction',
            field=models.TextField(max_length=200, null=True, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b', blank=True),
        ),
    ]
