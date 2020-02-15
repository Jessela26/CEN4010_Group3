from django.db import models

class Wishlist(models.Model):
    title = models.CharField(max_length=75) #Title of BOOK
    author = models.CharField(max_length=30) # Name of AUTHOR
    #picture =