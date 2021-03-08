from django.db import models

# Create your models here.

class Registration(models.Model):
    fullName = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=60)
    inn = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class User(models.Model):
    userName = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    def __str__(self):
        return self.name
