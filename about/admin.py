from django.contrib import admin
from . import models


class BannerImageAboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_count = models.BannerImageAbout.objects.count()
        return existing_count == 0

class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_count = models.AboutUs.objects.count()
        return existing_count == 0

# Register your models here.
admin.site.register(models.BannerImageAbout, BannerImageAboutAdmin)
admin.site.register(models.AboutUs, AboutUsAdmin)
admin.site.register(models.Team)
admin.site.register(models.Mission)

