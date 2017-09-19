# coding: utf-8
from django.db import models

class Category(models.Model):
    name = models.CharField('分类名', max_length=30)
    unique_name = models.CharField('name', max_length=30, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField('标签名', max_length=30)
    category = models.ForeignKey(Category, blank=True, null=True)
    unique_name = models.CharField('name', max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.name


class File(models.Model):

    title = models.CharField(max_length = 30)
    category = models.ForeignKey(Category, blank=True, null=True)
    tag = models.ForeignKey(Tag, blank=True, null=True)
    introduction = models.CharField('简介',max_length = 30, blank=True, null=True)
    FileField = models.FileField(upload_to='./library/files/')
    unique_name = models.CharField(max_length = 30, default='unique_name')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updata_time = models.DateTimeField('更新时间', auto_now=True)
    author = models.CharField(max_length = 30, default='admin')
    cover = models.ImageField('封面', upload_to='./library/files/cover/', null=True, blank=True)
    size = models.CharField('文件大小', max_length = 30, default=0)
    version = models.CharField('版本', max_length = 30, default=1.0, null=True, blank=True)
    bit = models.CharField('位数', max_length = 30, null=True, blank=True)
    amount_of_downloads = models.IntegerField('下载次数', default=0)
    developer = models.CharField('开发商', max_length = 30, null=True, blank=True)
    support_system = models.CharField('支持系统', max_length = 30, null=True, blank=True)
    language = models.CharField('语言', max_length = 30, null=True, blank=True)
    score = models.CharField('评分', max_length = 30, default=0)


    def __unicode__(self):
        return self.title



