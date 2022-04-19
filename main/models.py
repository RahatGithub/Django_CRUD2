from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    runs = models.CharField(max_length=20)
    wickets = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    franchise = models.CharField(max_length=100)
