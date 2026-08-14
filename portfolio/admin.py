from django.contrib import admin
from .models import Project, ServiceRate, PhotographerProfile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'description', 'category', 'is_featured'),
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_image_url'),
            'description': (
                'Upload an image directly, or upload on cloudinary.com and paste the image URL below. '
                'If both are set, the uploaded file is used.'
            ),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(super().get_fieldsets(request, obj))
        if obj:
            fieldsets[0][1]['fields'] = fieldsets[0][1]['fields'] + ('date_created',)
        return fieldsets


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
