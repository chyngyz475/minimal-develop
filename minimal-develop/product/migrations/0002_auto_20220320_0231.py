# Generated by Django 3.2.9 on 2022-03-19 19:31

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=image_cropping.fields.ImageCropField(blank=True, default='sys/employee_avatars/default.png', upload_to='sys/employee_avatars/', verbose_name='Превью товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('avatar', '270x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Маленькое превью товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='season',
            field=models.CharField(blank=True, choices=[('all', 'круглогодичный'), ('demseason', 'демисезон'), ('summer', 'летний'), ('winter', 'зимний')], max_length=50, null=True, verbose_name='Сезон одежды (Не обязательно)'),
        ),
    ]