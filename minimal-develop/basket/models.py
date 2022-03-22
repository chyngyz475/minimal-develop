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
from order.models import ItemBasketOrOrder 



class Basket(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True) 
    user_anonimus = models.IntegerField(default=-1,editable=False)
    
    items = models.ManyToManyField(ItemBasketOrOrder,'items_basket',
        verbose_name=_('Товары'))
    
    date_modified = models.DateTimeField(auto_now=True,verbose_name=_('Последнее изменение'))
    date_published = models.DateTimeField(auto_now_add=True,verbose_name=_('Создано'))

    
    def get_product_in_basket(self,product):
        return self.items.filter(item=product).first()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ItemBasketOrOrder.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs): 
        print("Saving profile") 
        if instance.basket is not None:
            print("Save profile")
            instance.basket.save()
        else:  
            ItemBasketOrOrder.objects.create(user=instance)
    
    
    class Meta:
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзина')