
from platform import release
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class MovieModel(models.Model):
    title = models.CharField (max_length=100)
    release_year = models.IntegerField()
    producer = models.CharField(max_length=100)
    is_watched = models.CharField (max_length=3, default='no')

    class Meta:
        db_table = 'movies'

        def __str__(self):
            return(f"{self.title} - {self.release} - {self.producer}")
        
        # def get_absolute_url(self):
        #     return reverse('mark-watched',kwargs={"pk":self.pk})
        




