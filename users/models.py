from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30, default='')

    def __unicode__(self):
        return self.username
