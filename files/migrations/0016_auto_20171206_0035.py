# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0015_auto_20171010_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='bad',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xb7\xae\xe8\xaf\x84'),
        ),
        migrations.AddField(
            model_name='file',
            name='good',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xa5\xbd\xe8\xaf\x84'),
        ),
    ]
