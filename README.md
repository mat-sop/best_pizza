# best_pizza
Restful API that allows voting for the best pizza. Service is temporarily hosted [here](https://18.184.185.80:8000).
Swagger docs is available [here](https://18.184.185.80:8000/swagger/)


### Requirements
Api and database can be started and configured using `docker` and `docker-compose`.


### Installation
```
docker-compose build
docker-compose up -d
```
After these commands service is running and can be accessed under `127.0.0.1:8000`
Service can be stopped by `docker-compose down`


### Endpoints
- `pizzas/` list of pizzas, creation of new pizza
- `pizzas/<pk: int>/` detail view or update of selected pizza
- `pizzas/<pk: int>/vote/` adds to number_of_votes field of selected pizza
- `restaurants/` list of restaurants, creation of new restaurant
- `restaurants/<pk: int>/` detail view or update of selected restaurant
- `toppings/` list of toppings, creation of new topping
- `swagger/` generated documentation of api
