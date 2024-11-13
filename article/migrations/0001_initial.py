# Generated by Django 4.2.2 on 2023-10-06 18:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('image', models.ImageField(help_text='لطفاً تصویری با ابعاد 1921 در 966  پیکسل وارد کنید', upload_to='image/article', verbose_name='تصویر')),
                ('content', ckeditor.fields.RichTextField(verbose_name='محتوا')),
                ('public', models.DateField(verbose_name='تاربخ')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('content', models.TextField(verbose_name='محتوا')),
            ],
            options={
                'verbose_name': 'نوار کناری',
                'verbose_name_plural': 'نوار کناری',
            },
        ),
    ]
