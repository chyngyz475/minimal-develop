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
from main import utility
from image_cropping import ImageRatioField
from image_cropping.utils import get_backend 
 

 
class DeliveryAdress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    region = models.CharField(  
        max_length=300,
        verbose_name=_('Область/край'),
        null=True,
        blank=True,
    ) 
    tower = models.CharField(  
        max_length=300,
        verbose_name=_('Населённый пункт'),
        null=True,
        blank=True,
    )
    street = models.CharField(   
        max_length=300,
        verbose_name=_('Улица'),
        null=True,
        blank=True,
    )
    number_house = models.IntegerField(   
        verbose_name=_('Номер дома'),
        null=True,
        blank=True,
    )
    number_flat = models.IntegerField(   
        verbose_name=_('Номер квартиры'),
        null=True,
        blank=True,
    )
    index_mail = models.IntegerField(   
        verbose_name=_('Индекс'),
        null=True,
        blank=True,
    )
    
    date_modified = models.DateTimeField(auto_now=True,verbose_name=_('Последнее изменение'))
    date_published = models.DateTimeField(auto_now_add=True,verbose_name=_('Создано'))

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            DeliveryAdress.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        if instance.deliveryadress is not None: 
            instance.deliveryadress.save()
        else:  
            DeliveryAdress.objects.create(user=instance)
    
    class Meta:
        verbose_name = _('Доставка')
        verbose_name_plural = _('Доставка')