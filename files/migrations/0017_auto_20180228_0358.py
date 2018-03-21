# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0016_auto_20171206_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='unique_name',
            field=models.CharField(default=b'unique_name', max_length=100),
        ),
    ]
