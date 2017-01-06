from django.apps import AppConfig

class AppConfig(AppConfig):
    name = 'foodlg.api'
    label = 'foodlg_api' 

default_app_config = 'foodlg.api.AppConfig'