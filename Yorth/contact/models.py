from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=50, verbose_name="تلفن")
    message = models.TextField(verbose_name="پیام" )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "اطلاعات تماس"
        verbose_name_plural = "اطلاعات تماس"

class BannerImage(models.Model):
    image = models.ImageField(upload_to="image/banner",help_text= "لطفاً تصویری با ابعاد 1921 در 966  پیکسل وارد کنید" ,verbose_name="تصویر بنر")

    class Meta:
        verbose_name = "تصویر بنر"
        verbose_name_plural = "تصویر بنر"

class Email(models.Model):
    email = models.EmailField(verbose_name="ایمیل", help_text="مثال: example@example.com")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "ایمیل"
        verbose_name_plural = "ایمیل ها‌"

class Address(models.Model):
    address = models.CharField(max_length=200, verbose_name="آدرس")
    link = models.CharField(max_length=9999,null=True, blank=True, verbose_name='لینک(اختیاری)')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس‌"



class Number(models.Model):
    number = models.CharField(max_length=20, verbose_name="شماره تماس", help_text="مثال: 09121234567")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "شماره تماس"
        verbose_name_plural = "شماره‌های تماس"