from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey('erp.Country', on_delete=models.CASCADE())
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey('erp.Country', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey('erp.City', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

