from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length= 100)
    slug = models.SlugField(null= True, blank= True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=False, default= timezone.now)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
