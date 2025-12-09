from django.contrib import admin
from django.utils.html import format_html
from .models import AboutMe, Experience, BombayShark, GalleryImage, Certification, ContactSubmission, CompanyLogo


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    fields = ['image', 'caption', 'order', 'image_preview']
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = "Preview"


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone', 'photo_preview']
    readonly_fields = ['created_at', 'updated_at', 'photo_preview']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'profile_photo', 'photo_preview')
        }),
        ('Contact Details', {
            'fields': ('email', 'phone')
        }),
        ('Social Media', {
            'fields': ('linkedin_url', 'instagram_url', 'twitter_url')
        }),
        ('About', {
            'fields': ('bio',)
        }),
        ('Resume', {
            'fields': ('resume',)
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def photo_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="max-height: 200px; border-radius: 10px;"/>', 
                             obj.profile_photo.url)
        return "No photo uploaded"
    photo_preview.short_description = "Photo Preview"
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not AboutMe.objects.exists()


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'start_date', 'end_date', 'is_current', 'order', 'logo_preview']
    list_filter = ['is_current', 'start_date']
    search_fields = ['role', 'company', 'description']
    list_editable = ['order']
    readonly_fields = ['created_at', 'updated_at', 'logo_preview']
    
    fieldsets = (
        ('Position Details', {
            'fields': ('company', 'role', 'start_date', 'end_date', 'is_current')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Visual', {
            'fields': ('company_logo', 'logo_preview')
        }),
        ('Display', {
            'fields': ('order',)
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def logo_preview(self, obj):
        if obj.company_logo:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.company_logo.url)
        return "No logo"
    logo_preview.short_description = "Logo Preview"


@admin.register(BombayShark)
class BombaySharkAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'age_groups', 'hero_preview']
    readonly_fields = ['created_at', 'updated_at', 'hero_preview']
    inlines = [GalleryImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'subtitle', 'hero_image', 'hero_preview')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Academy Details', {
            'fields': ('age_groups', 'locations', 'training_philosophy')
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def hero_preview(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="max-height: 200px; border-radius: 10px;"/>', 
                             obj.hero_image.url)
        return "No image"
    hero_preview.short_description = "Hero Image Preview"
    
    def has_add_permission(self, request):
        return not BombayShark.objects.exists()


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date', 'order', 'badge_preview']
    list_filter = ['issuing_organization', 'issue_date']
    search_fields = ['name', 'issuing_organization', 'credential_id']
    list_editable = ['order']
    readonly_fields = ['created_at', 'updated_at', 'badge_preview']
    
    fieldsets = (
        ('Certification Details', {
            'fields': ('name', 'issuing_organization', 'issue_date', 'credential_id')
        }),
        ('Visual', {
            'fields': ('certificate_image', 'badge_preview')
        }),
        ('Display', {
            'fields': ('order',)
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def badge_preview(self, obj):
        if obj.certificate_image:
            return format_html('<img src="{}" style="max-height: 80px;"/>', obj.certificate_image.url)
        return "No badge"
    badge_preview.short_description = "Badge Preview"


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'interest_type', 'submitted_at', 'is_read']
    list_filter = ['is_read', 'interest_type', 'age_group', 'submitted_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'phone', 'subject', 'message', 'interest_type', 
                       'age_group', 'submitted_at']
    list_editable = ['is_read']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Enrollment Details', {
            'fields': ('interest_type', 'age_group')
        }),
        ('Admin', {
            'fields': ('is_read', 'admin_notes', 'submitted_at')
        }),
    )
    
    def has_add_permission(self, request):
        # Prevent manual creation - should only come from form
        return False


@admin.register(CompanyLogo)
class CompanyLogoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'display_on_homepage', 'order', 'logo_preview']
    list_filter = ['display_on_homepage']
    search_fields = ['company_name']
    list_editable = ['order', 'display_on_homepage']
    readonly_fields = ['created_at', 'updated_at', 'logo_preview']
    
    fieldsets = (
        ('Company Details', {
            'fields': ('company_name', 'website_url')
        }),
        ('Logo', {
            'fields': ('logo', 'logo_preview')
        }),
        ('Display Settings', {
            'fields': ('display_on_homepage', 'order')
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 80px; max-width: 150px; object-fit: contain;"/>', 
                             obj.logo.url)
        return "No logo"
    logo_preview.short_description = "Logo Preview"


# Customize admin site header
admin.site.site_header = "Sumedh Rajarshi Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Your Portfolio Dashboard"
