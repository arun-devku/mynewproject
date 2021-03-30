from django.db import models

# Create your models here.
class UserDetais(models.Model):
    username=models.CharField(max_length=260)
    password=models.CharField(max_length=250)
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    phonenumber=models.IntegerField()

class UserDetailsfb(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    emailid=models.CharField(max_length=250)
    phonenumber=models.IntegerField()