from django.contrib import admin

from django.contrib import admin
from .models import ContactMessage, ServiceCategory, Service, ContactInfo,Review, SiteImage


admin.site.register(ContactInfo)
admin.site.register(Review)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)

@admin.register(SiteImage)
class SiteImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'category')
    list_filter = ('category',)
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    ordering = ('-created_at',)
