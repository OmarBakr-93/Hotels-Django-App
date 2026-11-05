from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=500)
    tags = TaggableManager()
    image = models.ImageField(upload_to='blog/')
    description = models.TextField(max_length=15000)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='post_category')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)

    
    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
            super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



