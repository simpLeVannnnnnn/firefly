# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20170801_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'./library/files/cover/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='FileField',
            field=models.FileField(upload_to=b'./library/files/'),
        ),
    ]
