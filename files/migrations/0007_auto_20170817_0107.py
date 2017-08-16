# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_auto_20170802_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='amount_of_downloads',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe6\xac\xa1\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='file',
            name='bit',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe4\xbd\x8d\xe6\x95\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='category',
            field=models.ForeignKey(blank=True, to='files.Category', null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='developer',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\xbc\x80\xe5\x8f\x91\xe8\x80\x85', blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='language',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe8\xaf\xad\xe8\xa8\x80', blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='score',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe8\xaf\x84\xe5\x88\x86', blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.CharField(default=0, max_length=30, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='file',
            name='support_system',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe6\x94\xaf\xe6\x8c\x81\xe7\xb3\xbb\xe7\xbb\x9f', blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='updata_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 16, 17, 7, 20, 330000, tzinfo=utc), verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='version',
            field=models.CharField(default=1.0, max_length=30, null=True, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac', blank=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='cover',
            field=models.ImageField(upload_to=b'./library/files/cover/', null=True, verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2', blank=True),
        ),
    ]
