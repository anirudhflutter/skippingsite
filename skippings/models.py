from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    reason = models.CharField(max_length=100)

class Product(models.Model):
    productname = models.CharField(max_length=100)
    productimage = models.CharField(max_length=100)
    productprice = models.IntegerField()


