# Generated by Django 4.2.2 on 2023-10-07 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0002_alter_article_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='لطفاً تصویری با ابعاد ۱۹۲۰ در ۱۱۵۰ پیکسل وارد کنید', upload_to='image/banner', verbose_name='تصویر')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
            ],
            options={
                'verbose_name': 'بنر صفحه اصلی',
                'verbose_name_plural': 'بنرهای صفحه اصلی',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='پیامی که می\u200cخواهید به اعضای خبرنامه ارسال شود را وارد کنید.', verbose_name='پیام')),
            ],
            options={
                'verbose_name': 'پیام به اعضای خبرنامه',
                'verbose_name_plural': 'پیام\u200cها به اعضای خبرنامه',
            },
        ),
        migrations.CreateModel(
            name='OurMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان')),
                ('text', models.TextField(blank=True, null=True, verbose_name='متن')),
            ],
            options={
                'verbose_name': 'ماموریت ما',
                'verbose_name_plural': 'ماموریت\u200cهای ما',
            },
        ),
        migrations.CreateModel(
            name='OurMissionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, help_text='لطفاً تصویری با ابعاد 217 در 153 پیکسل وارد کنید', null=True, upload_to='image/mission', verbose_name='تصویر ۱')),
                ('image2', models.ImageField(blank=True, help_text='لطفاً تصویری با ابعاد 271 در 191 پیکسل وارد کنید', null=True, upload_to='image/mission', verbose_name='تصویر ۲')),
                ('image3', models.ImageField(blank=True, help_text='لطفاً تصویری با ابعاد 271 در 191 پیکسل وارد کنید', null=True, upload_to='image/mission', verbose_name='تصویر ۳')),
                ('image4', models.ImageField(blank=True, help_text='لطفاً تصویری با ابعاد 339 در 236 پیکسل وارد کنید', null=True, upload_to='image/mission', verbose_name='تصویر ۴')),
                ('image5', models.ImageField(blank=True, help_text='لطفاً تصویری با ابعاد 217 در 153 پیکسل وارد کنید', null=True, upload_to='image/mission', verbose_name='تصویر ۵')),
                ('image6', models.ImageField(blank=True, help_text='لطفاً تصویری با ابعاد 179 در 126 پیکسل وارد کنید', null=True, upload_to='image/mission', verbose_name='تصویر ۶')),
            ],
            options={
                'verbose_name': 'تصاویر ماموریت ما',
                'verbose_name_plural': 'تصاویر ماموریت ما',
            },
        ),

        migrations.CreateModel(
            name='SubscribeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11, verbose_name='شماره تلفن')),
            ],
            options={
                'verbose_name': 'عضویت در خبرنامه',
                'verbose_name_plural': 'عضویت\u200cها در خبرنامه',
            },
        ),
        migrations.CreateModel(
            name='AricleList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='لطفاً تصویری با ابعاد 396 در 372 پیکسل وارد کنید', upload_to='image/article', verbose_name='تصویر')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article', verbose_name='مقاله')),
            ],
            options={
                'verbose_name': 'لیست مقالات',
                'verbose_name_plural': 'لیست مقالات',
            },
        ),
    ]