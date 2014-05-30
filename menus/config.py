from django.apps import AppConfig
from django.utils.importlib import import_module


class MenusConfig(AppConfig):
    name = 'menus'
    verbose_name = "Menus"

    def ready(self):
        import_module('menus.collections')
