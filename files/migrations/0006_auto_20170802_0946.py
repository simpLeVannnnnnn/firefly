# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20170802_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='auth',
        ),
        migrations.AddField(
            model_name='file',
            name='author',
            field=models.CharField(default=b'admin', max_length=30),
        ),
    ]
