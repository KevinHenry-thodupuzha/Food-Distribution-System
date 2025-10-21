from django.contrib import admin
from .models import FoodPost, Interest

@admin.register(FoodPost)
class FoodPostAdmin(admin.ModelAdmin):
    list_display = ['food_type', 'donor_name', 'location', 'quantity', 'price', 'is_available', 'user', 'created_at']
    list_filter = ['created_at', 'food_type', 'is_available']
    search_fields = ['food_type', 'donor_name', 'location']
    date_hierarchy = 'created_at'

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['user', 'food_post', 'contact_info', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'food_post__food_type', 'contact_info']
    date_hierarchy = 'created_at'
