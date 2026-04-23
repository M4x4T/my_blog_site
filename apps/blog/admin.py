from django.contrib import admin
from .models import Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title_en',)} 
    list_display = ('title_en', 'is_published', 'created_at')
    
    # This part creates the visual sections in your Admin panel
    fieldsets = (
        ('System', {'fields': ('slug', 'category', 'tags', 'is_published')}),
        ('English Content', {'fields': ('title_en', 'content_en')}),
        ('Turkish Content', {'fields': ('title_tr', 'content_tr')}),
        ('Russian Content', {'fields': ('title_ru', 'content_ru')}),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_tr', 'name_ru')
