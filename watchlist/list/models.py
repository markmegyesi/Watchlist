
from platform import release
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class MovieModel(models.Model):
    title = models.CharField (max_length=100)
    release_year = models.IntegerField()
    producer = models.CharField(max_length=100)
    

    class Meta:
        db_table = 'movielist'

    def __str__(self):
        return f"{self.title}"
    
    
        




