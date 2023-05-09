from django.contrib import admin
from django.db import models

from products.models import Product,Sliders,ProductsImage,Specialoffer
# Register your models here.

class ItemInline(admin.StackedInline):
    model = ProductsImage
    extra = 0


class ImageAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    readonly_fields=("id",)
    # list_display = ['__all__']




admin.site.register(Product,ImageAdmin)
admin.site.register(Sliders)
admin.site.register(Specialoffer)
  