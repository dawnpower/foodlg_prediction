from django.conf import settings
from django.db import models
import os

from foodlg.utils import getUploadToPath

class Photo(models.Model):    
    path = models.FileField(upload_to=getUploadToPath)
    description = models.CharField(max_length=1000,blank=True) 
    def __unicode__(self):
        return self.path.url   
