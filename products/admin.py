from django.contrib import admin
from django.db import models

from products.models import Product,Sliders,ProductsImage,Specialoffer,PopularProduct,PopularProductsImage
# Register your models here.

class ItemInline(admin.StackedInline):
    model = ProductsImage
    extra = 0

class ImageAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    readonly_fields=("id",)
    # list_display = ['__all__']
    

class ItemInlinepopular(admin.StackedInline):
    model = PopularProductsImage
    extra = 0

class Imagespopular(admin.ModelAdmin):
    inlines = [ItemInlinepopular]
    readonly_fields=("id",)


admin.site.register(Product,ImageAdmin)
admin.site.register(Sliders)
admin.site.register(Specialoffer),
admin.site.register(PopularProduct,Imagespopular)
  