from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from pizzas.models import Pizza, Restaurant, Topping
from pizzas.serializers import (PizzaSerializer, RestaurantSerializer,
                                ToppingSerializer)


class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ToppingList(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


@api_view(['GET'])
def pizza_vote(request, pk, format=None):
    try:
        pizza = Pizza.objects.get(pk=pk)
        pizza.number_of_votes += 1
        pizza.save()
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pizzas': reverse('pizza-list', request=request, format=format),
        'restaurants': reverse('restaurant-list', request=request, format=format),
        'toppings': reverse('topping-list', request=request, format=format)
    })
