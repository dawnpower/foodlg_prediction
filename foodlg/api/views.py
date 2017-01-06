#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import  HttpResponse, HttpResponseNotFound, JsonResponse, HttpResponseNotAllowed
from django.conf import settings
import requests as req
from .models import Dish 
from foodlg.utils import predict_file
# Create your views here.

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def nutrient_by_dish(request,dish_name):
    
    dish = Dish.objects.filter(name=dish_name.lower()).first()
    if dish:
        dish_nutrient_list = dish.nutrients.all()
        nutrients=[]
        result=dict(
                dish_name=dish.name,
                nutrients=nutrients,
                    )
        for dn in dish_nutrient_list:
            nutrient=dict(
                    id=dn.nutrient.id,
                    name=dn.nutrient.name,
                    group=dn.nutrient.group,
                    amount=dn.quantity,
                    unit=dn.unit,
                          )
            nutrients.append(nutrient)
        return JsonResponse(result) 
    else:
        return HttpResponse("dish not found!")

@csrf_exempt
def predict_dish(request):
    if request.method == 'POST':
        image = request.FILES['image']
        response,error = predict_file(image) 
        return HttpResponse(response)
    return HttpResponseNotAllowed 


@csrf_exempt
def predict_dish_json(request):
    if request.method == 'POST':
        image = request.FILES['image']
        response,error = predict_file(image) 
            
        dish_list=[]
        result= dict(
                      result='succeed',
                      data=dish_list
                      )
        if error:
            result['result']='failed'
            return JsonResponse(result)

        for dish in response.split("\n"):
            if not dish:
                continue
            dish_name = dish.split(":")[0]
            dish_prop = round(float(dish.split(":")[1])*100,2)
            dish_list.append({"name":dish_name,"prop":dish_prop})

        return JsonResponse(result)
    return HttpResponseNotAllowed 