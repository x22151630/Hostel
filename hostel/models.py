"""
Module for defining models.
"""
from django.db import models
 
class Hostel(models.Model):
    title = models.CharField(max_length=200)
    service_info = models.TextField() 
    image = models.URLField(blank=True, null=True)
 
    def __str__(self):
        return self.title + ""