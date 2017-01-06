from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import os, json, urllib, requests, datetime, time, zipfile, shutil

from .forms import  * 
from .models import *
from foodlg.utils import predict_file

def index(request):
    model={}
    if request.method == 'POST':
        form = AddPhotoForm(request.POST,request.FILES)
        if form.is_valid():
            photo = Photo()
            image=request.FILES['file']
            response,error = predict_file(image) 
            if error:
                model["message"]=response
            else:
                model['result']=True
                dish_list=[]
                for dish in response.split("\n"):
                    if not dish:
                        continue
                    dish_name = dish.split(":")[0]
                    dish_prop = round(float(dish.split(":")[1])*100,2)
                    dish_list.append({"name":dish_name,"prop":dish_prop})
                photo.path =image 
                photo.save()
                model['dish_list']=dish_list
                model['photo_url']=photo.path.url
        else:
            model['message']=form.errors.as_text()
    else:
        form = AddPhotoForm()
    model['form']=form
    return render(request, 'core/index.html', model)
   
def demo(request):
    return render(request, 'core/demo.html', {})

def example(request):
    return render(request, 'core/example.html', {'foodlist':food_list})

def handle_uploaded_file(f):
    tempFile = os.path.join(settings.IMAGE_TEMP_DIR,str(time.time()))
    z = zipfile.ZipFile(f)
    z.extractall(tempFile)
    return tempFile

food_list=[]
def getFoodList():
    global food_list
    food_list_path = os.path.join(settings.MEDIA_ROOT,"foodlist")
    food_name_list = os.listdir(food_list_path)
    food_name_list.sort()
    food_list=[]
    index =0
    for food_name in food_name_list:
        image_name_list = os.listdir(os.path.join(food_list_path,food_name))
        image_list = [os.path.join("foodlist",food_name,img) for img in image_name_list]
        food = dict(
                id = index,
                name=food_name,
                images = image_list,
                    )
        index+=1
        food_list.append(food)
    print food_list

getFoodList()