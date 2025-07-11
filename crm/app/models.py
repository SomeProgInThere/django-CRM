from django.db import models

# Create your models here.

class Record(models.Model):
    createdAt   = models.DateTimeField(auto_now_add=True)
    updatedAt   = models.DateTimeField(auto_now=True)
    username    = models.CharField(max_length=50)
    email       = models.EmailField(max_length=50)
    phone       = models.CharField(max_length=10)
    address     = models.CharField(max_length=100)
    city        = models.CharField(max_length=50)
    state       = models.CharField(max_length=50)
    zipcode     = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.username}'