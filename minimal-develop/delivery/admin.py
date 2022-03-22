from django.contrib import admin
from . import models 
 
@admin.register(models.DeliveryAdress)
class DeliveryAdress(admin.ModelAdmin): 
    list_display = ('user', 'region')
    ordering = ('-date_published', )