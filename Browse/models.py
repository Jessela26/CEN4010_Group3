from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=75)
    author = models.CharField(max_length=30)
    author_bio = models.CharField(max_length=5000, null=True)
    publisher = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000, null=True)
    date_published = models.CharField(max_length=50, null=True)
    rating = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    top_seller = models.BooleanField(null=True)
    genre = models.CharField(max_length=20, null=True)
