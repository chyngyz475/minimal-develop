# Generated by Django 3.2.9 on 2022-03-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryadress',
            name='index_mail',
            field=models.IntegerField(blank=True, null=True, verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='number_flat',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер квартиры'),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='number_house',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='region',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Область/край'),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='street',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='tower',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Населённый пункт'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='data_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
