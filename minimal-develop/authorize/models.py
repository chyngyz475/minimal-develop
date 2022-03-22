from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User 

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    GENDER_CHOICES = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )  
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICES,
        verbose_name='Пол'
        
    )
    data_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    
    date_modified = models.DateTimeField(auto_now=True,verbose_name=_('Последнее изменение'))
    date_published = models.DateTimeField(auto_now_add=True,verbose_name=_('Создано'))

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs): 
        print("Saving profile") 
        if instance.profile is not None:
            print("Save profile")
            instance.profile.save()
        else:  
            Profile.objects.create(user=instance)

    
    class Meta:
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профиль')