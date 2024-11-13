from django.db import models


# Create your models here.
# Create your models here.
class BannerImageAbout(models.Model):
    image = models.ImageField(upload_to="image/banner", help_text= "لطفاً تصویری با ابعاد 1921 در 966 پیکسل وارد کنید",)

    class Meta:
        verbose_name = "تصویر بنر درباره ما"
        verbose_name_plural = "تصویر بنر درباره ما"

class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    image = models.ImageField(upload_to="image/about", help_text= "لطفاً تصویری با ابعاد 518 در434 پیکسل وارد کنید", verbose_name= "تصویر")
    content = models.TextField(verbose_name="محتوا")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

class Mission(models.Model):
    icon = models.FileField(upload_to='icon', verbose_name="ایکون(اختیاری)", blank=True, null=True,
                            help_text="فایل آیکون مرتبط با مأموریت خود را انتخاب کنید.")
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="عنوان")
    text = models.TextField(null=True, blank=True, verbose_name="متن")

    def __str__(self):
        return self.title if self.title else "بدون عنوان"

    class Meta:
        verbose_name = "ماموریت"
        verbose_name_plural = "ماموریت‌ها"

class Team(models.Model):
    image = models.ImageField(upload_to="image/team", verbose_name="تصویر", help_text= "لطفاً تصویری با ابعاد 391 در 252 پیکسل وارد کنید",)
    fullname = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    job = models.CharField(max_length=100, verbose_name="سمت")
    instagram = models.CharField(max_length=1000, verbose_name="لینک پیج اینستاگرام(اختیاری)",blank=True, null=True)
    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "تیم"
        verbose_name_plural = "تیم"
