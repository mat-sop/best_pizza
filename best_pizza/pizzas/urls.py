from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from pizzas import views


schema_view = get_schema_view(
   openapi.Info(
      title="Best Pizza API",
   ),
   public=True,
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', views.api_root),
    path('pizzas/', views.PizzaList.as_view(), name='pizza-list'),
    path('pizzas/<int:pk>/', views.PizzaDetail.as_view(), name='pizza-detail'),
    path('pizzas/<int:pk>/vote/', views.pizza_vote, name='pizza-vote'),
    path('restaurants/', views.RestaurantList.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant-detail'),
    path('toppings/', views.ToppingList.as_view(), name='topping-list')
]
