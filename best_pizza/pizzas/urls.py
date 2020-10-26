from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from pizzas import views

urlpatterns = [
    path('', views.api_root),
    path('pizzas/', views.PizzaList.as_view(), name='pizza-list'),
    path('pizzas/<int:pk>/', views.PizzaDetail.as_view(), name='pizza-detail'),
    path('pizzas/<int:pk>/vote/', views.pizza_vote, name='pizza-vote'),
    path('restaurants/', views.RestaurantList.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant-detail'),
    path('toppings/', views.ToppingList.as_view(), name='topping-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)
