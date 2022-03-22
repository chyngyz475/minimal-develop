from django.contrib import admin
from . import models 
    

@admin.register(models.Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'phone_number')
    list_display_links = ('client_name', )
    ordering = ('-date_added', )

@admin.register(models.CmmSlider)
class CmmSliderAdmin(admin.ModelAdmin):
    list_editable = ('is_published',)
    image_display = ('image',)
    list_display_links = ('id', 'title')
    list_display_text =('text',)