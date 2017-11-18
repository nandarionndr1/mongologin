from django.db import models
from mongoengine import *
# Create your models here.
class User(Document):
    name = StringField(max_length=50)
    email = StringField(max_length=50)
    usrnm = StringField(max_length=50)
    pss = StringField(max_length=50)
    githuburl = StringField(max_length=50)
    bio = StringField(max_length=50)