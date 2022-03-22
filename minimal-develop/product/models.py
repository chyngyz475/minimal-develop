from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from matplotlib.pyplot import title 
from colorfield.fields import ColorField
from main import utility
from image_cropping import ImageRatioField, ImageCropField
from image_cropping.utils import get_backend 
from django.urls import reverse 

Season = (
        ('all', 'круглогодичный'),
        ('demseason', 'демисезон'),

        ('summer', 'летний'),
        ('winter', 'зимний')
    ) 

class ColorProduct(models.Model):
    color = ColorField(default='#FF0000')
    
    description = models.TextField( 
        verbose_name=_('Описание для админ панели'),
    )

    
    class Meta:
        verbose_name = _('Цвета товаров')
        verbose_name_plural = _('Цвета товаров') 

    def __str__(self) -> str:
        return f'{self.pk}: {self.description}'


class SizeProduct(models.Model):
    number_size = models.CharField( 
        max_length=4,
        verbose_name=_('Тип размера (XXS,XS и т.д)'),
    )  
    class Meta:
        verbose_name = _('Размер товара')
        verbose_name_plural = _('Размер') 

    def __str__(self) -> str:
        return f'{self.number_size}'
 

class CategoryProduct(models.Model):
    title = models.CharField(
        max_length=100, 
        verbose_name='Категория', 
    )
    
    def __str__(self) -> str:
        return f'{self.title}'
    class Meta:
        verbose_name = _('Категории товаров')
        verbose_name_plural = _('Категории товаров')

class Product(models.Model):   
    title = models.TextField( 
        verbose_name=_('Название товара'), 
        max_length=300
    )
    colors = models.ManyToManyField(ColorProduct
        ,'colors',
        verbose_name=_('Цвета товара'))
    sizes = models.ManyToManyField(SizeProduct,'sizes',
        verbose_name=_('Размеры товара')) 
        
    composition = models.TextField( 
        verbose_name=_('Состав (Не обязательно)'),
        null=True,
        blank=True
    )
    size_model = models.ForeignKey(SizeProduct, 
        on_delete=models.CASCADE,
        related_name='size_model',
        verbose_name=_('Размер на модели(Не обязательно)'),
        null=True,
        blank=True
    )
    
    category = models.ForeignKey(CategoryProduct, 
        on_delete=models.CASCADE,
        related_name='category',
        verbose_name=_('Категория товара'), 
    )

    growth_model = models.IntegerField(
        verbose_name=_('Рост модели(Не обязательно)'),
        null=True,
        blank=True
    )
    croi_model = models.IntegerField(
        verbose_name=_('Крой (Не обязательно)'),
        null=True,
        blank=True
    )
    season = models.CharField(
        max_length=50,
        choices=Season,
        verbose_name='Сезон одежды (Не обязательно)',
        null=True,
        blank=True
    )
    dlc_detals = models.TextField( 
        verbose_name=_('Дополнительные детали (Не обязательно)'),
        null=True,
        blank=True
    )
    description = models.TextField( 
        verbose_name=_('Описание товара (Не обязательно)'),
        null=True,
        blank=True
    )
    price = models.IntegerField(
        verbose_name=_('Цена'), 
        default=0
    )
    discount = models.IntegerField(
        verbose_name=_('Цена со скидкой'), 
        default=0
    )
    avatar = ImageCropField(
        upload_to='sys/employee_avatars/',
        verbose_name=_('Превью товара'),
        default='sys/employee_avatars/default.png',
        blank=True,
    ) 
    cropping = ImageRatioField('avatar', '270x360',verbose_name=_('Маленькое превью товара'))
   
    avatar_small = models.ImageField(
        upload_to='sys/employee_avatars/',
        verbose_name=_('Маленькое превью товара'),
        default='sys/employee_avatars/default.png',
        blank=True,  
        editable=False
    )
    is_discount = models.BooleanField(
        verbose_name=_('Цена по скидке?'), 
        default=False
    )
    is_public = models.BooleanField(
        verbose_name=_('Опубликован?'), 
        default=True
    )
    
   
    date_modified = models.DateTimeField(auto_now=True,verbose_name=_('Последнее изменение'))
    date_published = models.DateTimeField(auto_now_add=True,verbose_name=_('Создано'))
    
  

    def save(self, *args, **kwargs):  
            print(self.avatar_small) 
            print(self.cropping)  
            if(self.cropping):
                new_image = utility.cropping(self.avatar,self.cropping,quality=70)  
                self.avatar_small = new_image
            
            super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = _('Товары')
        verbose_name_plural = _('Товары')
 


class ImageItem(models.Model):
    image = models.ImageField(
        upload_to='sys/employee_avatars/',
        verbose_name=_('Маленькая Аватар сотрудника'),
        default='sys/employee_avatars/default.png',
        help_text=_('Автоматически добавляется при добавление основого, вы можете изменить его'),
        blank=True,   
    )
    cropping = ImageRatioField('image', '270x360',verbose_name=_('Маленькая Аватар сотрудника'))
    item = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='images_set', 
    )
    
    date_modified = models.DateTimeField(auto_now=True,verbose_name=_('Последнее изменение'))
    date_published = models.DateTimeField(auto_now_add=True,verbose_name=_('Создано'))

    def save(self, *args, **kwargs):   
            if(self.cropping):
                self.image = utility.cropping(self.image,self.cropping,quality=70)   
            
            super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.image}'
    class Meta:
        verbose_name = _('Фото товара')
        verbose_name_plural = _('Фото товара')
 


class Discount(models.Model):
    discount_text  = models.CharField( 
        max_length=3,
        verbose_name=_('Лейбл на товаре (Хит,10%,20% и т.д)'),
    )  
    discount_price  = models.IntegerField(   
        verbose_name=_('Скидка в процентах'),
        help_text=_('Сумма товаров снижается на указанный процент') 
    )   
    discounts = models.ManyToManyField(Product,'discounts',
        verbose_name=_('Товары'))

    
    date_modified = models.DateTimeField(auto_now=True,verbose_name=_('Последнее изменение'))
    date_published = models.DateTimeField(auto_now_add=True,verbose_name=_('Создано'))

    class Meta:
        verbose_name = _('Система скидок')
        verbose_name_plural = _('Система скидок')

    def __str__(self) -> str:
        return str(self.text)


     