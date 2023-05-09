from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'number', 'email', 'product', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
