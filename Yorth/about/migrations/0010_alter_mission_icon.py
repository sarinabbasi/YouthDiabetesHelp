# Generated by Django 4.2.2 on 2023-10-09 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_mission_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='icon',
            field=models.FileField(blank=True, help_text='فایل آیکون مرتبط با مأموریت خود را انتخاب کنید.', null=True, upload_to='icon', verbose_name='ایکون(اختیاری)'),
        ),
    ]
