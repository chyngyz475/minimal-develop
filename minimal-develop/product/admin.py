from django.contrib import admin
from . import models
from image_cropping import ImageCroppingMixin

admin.site.register(models.ColorProduct)  
admin.site.register(models.SizeProduct) 
admin.site.register(models.CategoryProduct) 



class ImageItemInline(ImageCroppingMixin,admin.StackedInline):
    model = models.ImageItem
    extra = 0

@admin.register(models.Product) 
class ItemAdmin(ImageCroppingMixin,admin.ModelAdmin): 
    inlines = [
        ImageItemInline
    ]