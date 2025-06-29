from django.contrib import admin
from .models import Destination
# Register your models here.
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'best_time_to_visit', 'created_at','updated_at']
    list_filter = ['created_at','updated_at']
    search_fields = ['name', 'location', 'description']
    prepopulated_fields = {'slug': ('name',)}