from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('latest', 'Latest Work'),
        ('fashion', 'Fashion'),
        ('editorial', 'Editorial'),
    ]

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='latest')
    cover_image = models.ImageField(upload_to='projects/', storage=MediaCloudinaryStorage(), blank=True)
    cover_image_url = models.URLField(
        blank=True,
        help_text='Optional. Upload on cloudinary.com, then paste the image URL here.',
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Show this project in the homepage hero. Only one project can be featured at a time.",
    )
    date_created = models.DateField(auto_now_add=True)

    @property
    def cover_image_display(self):
        if self.cover_image:
            return self.cover_image.url
        return self.cover_image_url

    def save(self, *args, **kwargs):
        if self.is_featured:
            Project.objects.filter(is_featured=True).exclude(pk=self.pk).update(is_featured=False)
        super().save(*args, **kwargs)

    def __str__(self):        return self.title


class ServiceRate(models.Model):
    service_name = models.CharField(max_length=100)  # e.g., "Editorial Lookbook"
    price = models.CharField(max_length=50)           # e.g., "$1,200 / day" or "KSh 50,000"
    description = models.TextField()
    features = models.TextField(help_text="Separate features with commas or newlines")

    def __str__(self):
        return self.service_name


class PhotographerProfile(models.Model):
    name = models.CharField(max_length=100, default="YOUR NAME")
    label = models.CharField(max_length=100, default="// EDITOR & PHOTOGRAPHER")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', storage=MediaCloudinaryStorage(), blank=True, null=True)
    profile_image_url = models.URLField(
        blank=True,
        help_text='Optional. Upload on cloudinary.com, then paste the image URL here.',
    )
    instagram_url = models.URLField(blank=True, null=True)
    twitter_x_url = models.URLField(blank=True, null=True)

    @property
    def profile_image_display(self):
        if self.profile_image:
            return self.profile_image.url
        return self.profile_image_url

    class Meta:
        verbose_name = "Photographer Profile"
        verbose_name_plural = "Photographer Profile"

    def __str__(self):
        return self.name
