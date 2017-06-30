from django.db import models
from mongoengine import *

class File(mongoengine.Document):
    
    title = mongoengine.StringField(required=True)
    url = mongoengine.FileField(upload_to = './upload/')

