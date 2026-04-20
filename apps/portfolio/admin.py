from django.contrib import admin # <--- This fixes the NameError
from .models import Project      # <--- Import Project, not Article

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'tools_used', 'created_at')
    
    fieldsets = (
        ('Project Links & Tech', {
            'fields': ('tools_used', 'github_url', 'notebook_url')
        }),
        ('English', {
            'fields': ('title_en', 'description_en')
        }),
        ('Turkish', {
            'fields': ('title_tr', 'description_tr')
        }),
        ('Russian', {
            'fields': ('title_ru', 'description_ru')
        }),
    )