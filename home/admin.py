from django.contrib import admin
from .models import SubscribeModel, HomeBanner, OurMission, OurMissionImage, AricleList, Message


class HomeBannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_count = HomeBanner.objects.count()
        return existing_count == 0


class OurMissionImageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_count = OurMissionImage.objects.count()
        return existing_count == 0

admin.site.register(Message)
admin.site.register(SubscribeModel)
admin.site.register(HomeBanner, HomeBannerAdmin)
admin.site.register(OurMission)
admin.site.register(OurMissionImage, OurMissionImageAdmin)
admin.site.register(AricleList)
