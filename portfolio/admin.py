from django.contrib import admin
from .models import Project, ServiceRate, PhotographerProfile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'description', 'category', 'is_featured', 'date_created'),
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_image_url'),
            'description': (
                'Upload an image directly, or upload on cloudinary.com and paste the image URL below. '
                'If both are set, the uploaded file is used.'
            ),
        }),
    )


@admin.register(PhotographerProfile)
class PhotographerProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'label', 'bio', 'instagram_url', 'twitter_x_url'),
        }),
        ('Profile Image', {
            'fields': ('profile_image', 'profile_image_url'),
            'description': (
                'Upload an image directly, or upload on cloudinary.com and paste the image URL below. '
                'If both are set, the uploaded file is used.'
            ),
        }),
    )


admin.site.register(ServiceRate)
