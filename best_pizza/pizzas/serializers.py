from rest_framework import serializers

from pizzas.models import Pizza, Restaurant, Topping


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'website', 'address']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id', 'name']


class PizzaSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    toppings = serializers.PrimaryKeyRelatedField(many=True, queryset=Topping.objects.all())
    number_of_votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pizza
        fields = ['id', 'name', 'description', 'photo', 'restaurant', 'toppings', 'number_of_votes']
