from rest_framework import serializers

from pizzas.models import Pizza, Restaurant, Topping


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['name']


class PizzaSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    restaurant = RestaurantSerializer()
    toppings = ToppingSerializer(many=True)
    number_of_votes = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        restaurant_data = validated_data.pop("restaurant")
        restaurant = Restaurant.objects.get_or_create(**restaurant_data)[0]

        toppings_data = validated_data.pop("toppings")
        toppings = []
        for topping_data in toppings_data:
            toppings.append(Topping.objects.get_or_create(**topping_data)[0])

        pizza = Pizza.objects.create(restaurant=restaurant, **validated_data)
        pizza.toppings.add(*toppings)
        pizza.save()
        return pizza

    def update(self, instance, validated_data):
        restaurant_data = validated_data.pop("restaurant")
        toppings_data = validated_data.pop("toppings")

        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)

        restaurant = instance.restaurant
        restaurant.name = restaurant_data.get("name", restaurant.name)
        restaurant.save()

        toppings = []
        for topping_data in toppings_data:
            toppings.append(Topping.objects.get_or_create(**topping_data)[0])
        instance.toppings.set(toppings)
        instance.save()

        return instance
