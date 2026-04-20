from django.contrib import admin
from .models import Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # We tell Django to use 'title_en' to create the URL slug
    prepopulated_fields = {'slug': ('title_en',)} 
    list_display = ('title_en', 'category', 'is_published')
    
    fieldsets = (
        ('System', {'fields': ('slug', 'category', 'tags', 'is_published', 'created_at')}),
        ('English', {'fields': ('title_en', 'content_en')}),
        ('Turkish', {'fields': ('title_tr', 'content_tr')}),
        ('Russian', {'fields': ('title_ru', 'content_ru')}),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_tr', 'name_ru')
