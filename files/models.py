from django.db import models

class File(models.Model):

    title = models.CharField(max_length = 30)
    FileField = models.FileField(upload_to='./library/')
    unique_name = models.CharField(max_length = 30, default='unique_name')
