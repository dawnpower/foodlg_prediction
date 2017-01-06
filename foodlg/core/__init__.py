from django.apps import AppConfig

class AppConfig(AppConfig):
    name = 'foodlg.core'
    label = 'foodlg_core' 

default_app_config = 'foodlg.core.AppConfig'