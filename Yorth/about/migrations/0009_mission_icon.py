# Generated by Django 4.2.2 on 2023-10-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_team_instagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='icon',
            field=models.FileField(default=1, help_text='فایل آیکون مرتبط با مأموریت خود را انتخاب کنید.', upload_to='icon', verbose_name='ایکون(اختیاری)'),
            preserve_default=False,
        ),
    ]