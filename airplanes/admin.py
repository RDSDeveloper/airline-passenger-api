from django.contrib import admin
from .models import Airplane

@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    pass