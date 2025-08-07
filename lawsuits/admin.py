from django.contrib import admin
from .models import Lawsuit

@admin.register(Lawsuit)
class LawsuitAdmin(admin.ModelAdmin):
    list_display = ['title', 'client_name', 'case_type', 'status', 'created_at']
    list_filter = ['status', 'case_type', 'created_at']
    search_fields = ['title', 'client_name', 'description']
