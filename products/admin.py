from django.contrib import admin
from .models import CategoryModel, ProductModel, ImageModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(ImageModel)
