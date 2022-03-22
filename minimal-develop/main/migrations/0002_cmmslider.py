# Generated by Django 3.2 on 2022-03-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CmmSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmm_img', models.ImageField(upload_to='')),
                ('cmm_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('cmm_text', models.CharField(max_length=200, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'slider',
            },
        ),
    ]
