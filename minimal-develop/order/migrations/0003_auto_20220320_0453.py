# Generated by Django 3.2.9 on 2022-03-19 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_auto_20220320_0242'),
        ('order', '0002_alter_order_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemBasketOrOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Цена за товар')),
                ('count', models.IntegerField(verbose_name='Кол-во шт товара')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='product.product', verbose_name='Товар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ItemOrder',
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='items_order', to='order.ItemBasketOrOrder', verbose_name='Товары'),
        ),
    ]
