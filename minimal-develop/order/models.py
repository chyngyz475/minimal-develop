from tkinter import CASCADE
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User 
from colorfield.fields import ColorField 
from image_cropping import ImageRatioField
from image_cropping.utils import get_backend 
#Apps project
from main import utility
from product.models import Product 

class ItemBasketOrOrder(models.Model):  
    item = models.ForeignKey(Product,related_name='item',verbose_name=_('Товар'), on_delete=models.CASCADE)
    price = models.IntegerField(   
        verbose_name=_('Цена за товар'), 
    )
    count = models.IntegerField(   
        verbose_name=_('Кол-во шт товара'),
        default=1
    )

class Order(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    items = models.ManyToManyField(ItemBasketOrOrder,'items_order',
        verbose_name=_('Товары'))
    
    date_modified = models.DateTimeField(auto_now=True,verbose_name=_('Последнее изменение'))
    date_published = models.DateTimeField(auto_now_add=True,verbose_name=_('Создано'))

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Order.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs): 
        print("Saving profile") 
        if instance.order is not None:
            print("Save profile")
            instance.order.save()
        else:  
            Order.objects.create(user=instance)
    
    
    class Meta:
        verbose_name = _('Заказы')
        verbose_name_plural = _('Заказы')