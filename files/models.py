# coding: utf-8
from django.db import models



class File(models.Model):

    title = models.CharField(max_length = 30)
    FileField = models.FileField(upload_to='./library/files/')
    unique_name = models.CharField(max_length = 30, default='unique_name')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    author = models.CharField(max_length = 30, default='admin')
    cover = models.ImageField(upload_to='./library/files/cover/', null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField('分类名', max_length=30)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('标签名', max_length=30)

    def __str__(self):
        return self.name
