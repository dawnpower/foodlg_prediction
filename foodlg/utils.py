import datetime, os
from django.conf import settings
import requests as req

def getUploadToPath(instance,filename):
    today = datetime.datetime.today()
    upload_path = 'upload/%d%d/%s' % (today.year,today.month,filename)
    return upload_path

def getFullPath(filename):
    return os.path.join(settings.MEDIA_ROOT,filename)

def jdefault(o):
    '''
        make a default json encoder function, just call to_json method
    '''
    return o.to_JSON()

def predict_file(file):
    if file and allowed_file(file.name):
        url = settings.SINGA_SERVER_API
        files = {'image':(file.name,file)}
        r=req.post(url,files=files)
        response = r.text
        return response,False 
    else:
        return "Only jpg file is allowed!",True

def allowed_file(filename):
    allowd_extensions_ = set(['jpg', 'jpeg','JPG','JPEG'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allowd_extensions_


    
