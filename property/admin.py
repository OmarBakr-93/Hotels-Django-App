from django.contrib import admin
from .models import Property, PropertyBook, PropertyImage, Place, Category, PropertyReview

# Register your models here.

admin.site.register(Property)
admin.site.register(PropertyBook)
admin.site.register(PropertyImage)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
