from django.db import models

from foodlg.utils import getUploadToPath
import datetime

class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,blank=True,null=True)
    source = models.CharField(max_length=255,blank=True,null=True)

class Nutrient(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50,blank=True,null=True)

class DishNutrient(models.Model):
    dish = models.ForeignKey(Dish, related_name='nutrients')
    nutrient = models.ForeignKey(Nutrient)
    unit = models.CharField(max_length=10)
    quantity = models.FloatField(default=0)