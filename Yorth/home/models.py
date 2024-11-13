from django.db.models.signals import post_save
from django.dispatch import receiver
import ghasedakpack
from django.db import models
from article.models import Article

class HomeBanner(models.Model):
    image = models.ImageField(upload_to="image/banner", verbose_name="تصویر", help_text="لطفاً تصویری با ابعاد ۱۹۲۰ در ۱۱۵۰ پیکسل وارد کنید")
    title = models.CharField(max_length=100, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بنر صفحه اصلی"
        verbose_name_plural = "بنرهای صفحه اصلی"

class OurMissionImage(models.Model):
    image1 = models.ImageField(upload_to="image/mission", null=True, blank=True, help_text= "لطفاً تصویری با ابعاد 217 در 153 پیکسل وارد کنید", verbose_name= "تصویر ۱")
    image2 = models.ImageField(upload_to="image/mission", null=True, blank=True, help_text="لطفاً تصویری با ابعاد 271 در 191 پیکسل وارد کنید" , verbose_name="تصویر ۲")
    image3 = models.ImageField(upload_to="image/mission", null=True, blank=True, help_text="لطفاً تصویری با ابعاد 271 در 191 پیکسل وارد کنید" , verbose_name="تصویر ۳")
    image4 = models.ImageField(upload_to="image/mission", null=True, blank=True, help_text="لطفاً تصویری با ابعاد 339 در 236 پیکسل وارد کنید" , verbose_name="تصویر ۴")
    image5 = models.ImageField(upload_to="image/mission", null=True, blank=True, help_text="لطفاً تصویری با ابعاد 217 در 153 پیکسل وارد کنید",  verbose_name="تصویر ۵")
    image6 = models.ImageField(upload_to="image/mission", null=True, blank=True, help_text="لطفاً تصویری با ابعاد 179 در 126 پیکسل وارد کنید",  verbose_name="تصویر ۶")

    def __str__(self):
        return "تصاویر ماموریت ما"

    class Meta:
        verbose_name = "تصاویر ماموریت ما"
        verbose_name_plural = "تصاویر ماموریت ما"

class OurMission(models.Model):
    icon = models.FileField(upload_to='icon', verbose_name="ایکون(اختیاری)", blank=True, null=True,
                            help_text="فایل آیکون مرتبط با مأموریت خود را انتخاب کنید.")
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="عنوان")
    text = models.TextField(null=True, blank=True, verbose_name="متن")

    def __str__(self):
        return self.title if self.title else "بدون عنوان"

    class Meta:
        verbose_name = "ماموریت ما"
        verbose_name_plural = "ماموریت‌های ما"

class AricleList(models.Model):
    image = models.ImageField(upload_to="image/article", verbose_name="تصویر" ,help_text="لطفاً تصویری با ابعاد 396 در 372 پیکسل وارد کنید")
    title = models.CharField(max_length=100, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="مقاله")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "لیست مقالات"
        verbose_name_plural = "لیست مقالات"


class SubscribeModel(models.Model):
    number = models.CharField(max_length=11, verbose_name="شماره تلفن")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "عضویت در خبرنامه"
        verbose_name_plural = "عضویت‌ها در خبرنامه"


class Message(models.Model):
    message = models.TextField(
        verbose_name="پیام",
        help_text="پیامی که می‌خواهید به اعضای خبرنامه ارسال شود را وارد کنید."
    )

    def __str__(self):
        return f"پیام به اعضای خبرنامه: {self.message[:30]}"  # You can adjust the length as needed

    class Meta:
        verbose_name = "پیام به اعضای خبرنامه"
        verbose_name_plural = "پیام‌ها به اعضای خبرنامه"


@receiver(post_save, sender=Message)
def send_message_to_subscribers(sender, instance, created, **kwargs):
    if created:
        subscribers = SubscribeModel.objects.all()
        sms = ghasedakpack.Ghasedak("815fd62100f7a0e93271a74e3d418ec6818758cc8a4dbee1edf38a2868da0334")

        for subscriber in subscribers:

            response = sms.send({'message': instance.message, 'receptor': subscriber.number, 'linenumber': '10008566'})
            if response:
                print(f"Message successfully sent to {subscriber.number}")
            else:
                print(f"Failed to send the message to {subscriber.number}")

