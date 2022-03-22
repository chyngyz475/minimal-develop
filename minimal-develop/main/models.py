from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators


class Consultation(models.Model):
    client_name = models.CharField(
        max_length=128,
        verbose_name=_('Имя клиента'),
        null=True,
        blank=True
    )
    phone_number = models.CharField(  # TODO: Найти хороший способ валидации номеров.
        max_length=16,
        verbose_name=_('Номер телефона'),
    )
    date_added = models.DateField(
        verbose_name=_('Дата заявки'),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('Консультация')
        verbose_name_plural = _('Консультации')
        ordering = ['-date_added']
        get_latest_by = 'date_added'

    def __str__(self) -> str:
        return f'{self.client_name}#{self.pk}'
 
 