# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_auto_20170817_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='tag',
            field=models.ForeignKey(blank=True, to='files.Tag', null=True),
        ),
    ]
