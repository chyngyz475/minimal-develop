# Generated by Django 3.2.9 on 2022-01-26 15:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_on_market', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Лет на рынке')),
                ('count_operations', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Кол-во операций под общим наркозом')),
                ('count_doctors', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Кол-во профессиональных врачей')),
                ('count_patients', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Кол-во пацинатов в год')),
                ('enabled_partners', models.BooleanField(default=False, help_text='Включает или отключает блок партнеров на сайте.', verbose_name='Отображать партнеров')),
                ('code_in_html', models.TextField(blank=True, help_text='Сюда можно вставить код Яндекс метрики и Google Analytics', null=True, verbose_name='Добавить скрипты в HEAD')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
        migrations.CreateModel(
            name='PhoneAndAddres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('phone_number', models.TextField(verbose_name='Номер телефона')),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_and_address_set', related_query_name='phone_and_address', to='global_setting.sitesetting')),
            ],
            options={
                'verbose_name': 'Телефон и адрес',
                'verbose_name_plural': 'Телефоны и адреса',
            },
        ),
    ]
