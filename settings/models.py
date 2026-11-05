from django.db import models

# Create your models here.


class Setting(models.Model):
    site_name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='settings/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    description = models.TextField(max_length=10000)
    fb_link = models.URLField(max_length=250)
    Twitter_link = models.URLField(max_length=250)
    instagram_link = models.URLField(max_length=250)

    def __str__(self):
        return self.site_name
    