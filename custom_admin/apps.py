from django.apps import AppConfig


class CustomAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_admin'


# from suit.apps import DjangoSuitConfig


# class SuitConfig(DjangoSuitConfig):
#    layout = 'horizontal'
