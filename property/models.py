from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Property(models.Model):
    name = models.CharField(max_length=250)
    main_image = models.ImageField(upload_to='property/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='property_places')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='property_category')
    slug = models.SlugField(max_length=250, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name



class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_images')
    image = models.ImageField(upload_to="property_images/")

    def __str__(self):
        return self.property.name


class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class PropertyReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property_reviews')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_reviews')
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property.name

COUNT = {
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
}

class PropertyBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property_books')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_books')
    date_from = models.DateTimeField(default=timezone.now)
    date_to = models.DateTimeField(default=timezone.now)
    guest = models.IntegerField(default=1, choices=COUNT)
    children = models.IntegerField(default=0, choices=COUNT)

    def __str__(self):
        return self.property.name




