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

class Logindetails(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250) 

class Details(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    phonenumber=models.IntegerField()
    user=models.ForeignKey(Logindetails,on_delete=models.CASCADE)

class Student(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    contactnumber=models.BigIntegerField()
    dateofbirth=models.DateField()

class propic(models.Model):
    propicture=models.FileField(upload_to='profile/')
    user=models.ForeignKey(Logindetails,on_delete=models.CASCADE)



class Images(models.Model):
    picture=models.FileField(upload_to='images/')