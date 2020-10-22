from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)


class Topping(models.Model):
    name = models.CharField(max_length=100)


class Pizza(models.Model):
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    restaurant = models.ForeignKey(Restaurant, blank=True, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)
    number_of_votes = models.PositiveIntegerField(default=0)
