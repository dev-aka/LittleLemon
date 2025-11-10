from django.apps import AppConfig
from .models import Booking, Menu
from django.contrib import admin


class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'

admin.site.register(Booking)
admin.site.register(Menu)