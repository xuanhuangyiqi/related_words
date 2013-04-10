#coding: utf-8
from django.db import models

class Record(models.Model):
    url = models.CharField( max_length=100 )
    word = models.CharField( max_length=100 )
    center = models.CharField( max_length=20 )
    title = models.CharField( max_length=20 )
