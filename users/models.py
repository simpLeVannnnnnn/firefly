from mongoengine import *

class User(mongoengine.Document):
    username = mongoengine.StringField()
    password = mongoengine.StringField(required=True)

    def __unicode__(self):
        return self.username
