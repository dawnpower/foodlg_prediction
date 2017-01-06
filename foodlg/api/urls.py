from django.conf.urls import url, include

from .views import * 

urlpatterns = [
    url(r'^nutrient_by_dish/(?P<dish_name>.+)$', nutrient_by_dish, name="nutrient_by_dish"),
    url(r'^predict_dish$', predict_dish, name="predict_dish"),
    url(r'^predict_dish_json$', predict_dish_json, name="predict_dish_json"),
]
