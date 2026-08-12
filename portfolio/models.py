from django.db import models

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
    cover_image = models.ImageField(upload_to='projects/')
    is_featured = models.BooleanField(default=False, help_text="Check this to feature this photo on the homepage hero section")
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


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
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    twitter_x_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Photographer Profile"
        verbose_name_plural = "Photographer Profile"

    def __str__(self):
        return self.name