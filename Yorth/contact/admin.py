from django.contrib import admin
from .models import ContactModel, Number, Address, Email, BannerImage



class NumberAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_count = Number.objects.count()
        return existing_count <= 2


class AddressAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_count = Address.objects.count()
        return existing_count == 0


class EmailAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_count = Email.objects.count()
        return existing_count <= 2


class BannerImageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        existing_count = BannerImage.objects.count()
        return existing_count == 0


# Register your models here.
admin.site.register(ContactModel)
admin.site.register(Number, NumberAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(BannerImage, BannerImageAdmin)
