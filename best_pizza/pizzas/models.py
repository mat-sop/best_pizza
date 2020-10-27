from django.conf import settings
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    address = models.CharField(max_length=250, blank=True)


class Topping(models.Model):
    name = models.CharField(max_length=100)


class Pizza(models.Model):
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(null=True)
    restaurant = models.ForeignKey(Restaurant, blank=True, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)
    number_of_votes = models.PositiveIntegerField(default=0)
