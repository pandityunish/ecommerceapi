from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'date']

admin.site.register(Feedback, FeedbackAdmin)
