from django.db import models

# Create your models here.
#This is the movie model
class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='movie/images/')
    url=models.URLField(blank=True)
