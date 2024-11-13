from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    image = models.ImageField(upload_to="image/article", verbose_name="تصویر", help_text= "لطفاً تصویری با ابعاد 1921 در 966  پیکسل وارد کنید",)
    content = RichTextField(verbose_name="محتوا")
    public = models.DateField(verbose_name='تاربخ', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

class Sidebar(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نوار کناری"
        verbose_name_plural = "نوار کناری"
