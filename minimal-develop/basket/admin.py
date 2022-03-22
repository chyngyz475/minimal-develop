from django.contrib import admin
from . import models
from image_cropping import ImageCroppingMixin
 
@admin.register(models.Basket)
class BasketAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        """
        Метод проверки прав на добавление.
        По умолчанию запрещаем добавление новых записей.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Метод проверки прав на удаление.
        По умолчанию запрещаем удаление записей.
        """
        return False

