from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=75)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True)
    year_published = models.DateField(max_length=50, null=True)
    rating = models.IntegerField(null=True)
