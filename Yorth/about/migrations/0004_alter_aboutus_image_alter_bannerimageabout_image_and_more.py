# Generated by Django 4.2.2 on 2023-08-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_aboutus_options_alter_bannerimageabout_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(help_text='لطفاً تصویری با ابعاد 518 در434 پیکسل وارد کنید', upload_to='image/about', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='bannerimageabout',
            name='image',
            field=models.ImageField(help_text='لطفاً تصویری با ابعاد 1921 در 966 پیکسل وارد کنید', upload_to='image/banner'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(help_text='لطفاً تصویری با ابعاد 391 در 252 پیکسل وارد کنید', upload_to='image/team', verbose_name='تصویر'),
        ),
    ]
