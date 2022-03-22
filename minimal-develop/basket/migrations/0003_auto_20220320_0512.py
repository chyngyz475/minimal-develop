# Generated by Django 3.2.9 on 2022-03-19 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AddField(
            model_name='basket',
            name='user_anonimus',
            field=models.IntegerField(default=-1, editable=False),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]