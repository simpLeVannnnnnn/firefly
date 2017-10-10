# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0014_auto_20171004_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='FileField',
            field=models.FileField(upload_to=b'./library/files/', verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6'),
        ),
        migrations.AlterField(
            model_name='file',
            name='introduction',
            field=models.TextField(max_length=250, null=True, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b', blank=True),
        ),
    ]
