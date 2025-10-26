# ...existing code...
from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)  # permite NULL temporariamente
    body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_on = models.DateTimeField(auto_now_add=True, null=True)  # permite NULL temporariamente

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)