# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
