from django.urls import path

from pizzas import views

urlpatterns = [
    path('pizzas/', views.PizzaList.as_view()),
    path('pizzas/<int:pk>/', views.PizzaDetail.as_view()),
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view()),
    path('toppings/', views.ToppingList.as_view())
]


