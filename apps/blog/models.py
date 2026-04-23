from django.db import models
from django.utils import timezone
from django.utils.translation import get_language


class Category(models.Model):
    name_en = models.CharField(max_length=100)
    name_tr = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)

    @property
    def translated_name(self):
        lang = get_language()
        if lang:
            lang = lang.split('-')[0]  # 'en-us' → 'en'
        return getattr(self, f'name_{lang}', self.name_en) or self.name_en

    def __str__(self):
        return self.name_en


class Article(models.Model):
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    title_en = models.CharField(max_length=200)
    content_en = models.TextField()
    title_tr = models.CharField(max_length=200, blank=True)
    content_tr = models.TextField(blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    content_ru = models.TextField(blank=True)

    @property
    def translated_title(self):
        lang = get_language()
        if lang:
            lang = lang.split('-')[0]
        return getattr(self, f'title_{lang}', self.title_en) or self.title_en

    @property
    def translated_content(self):
        lang = get_language()
        if lang:
            lang = lang.split('-')[0]
        return getattr(self, f'content_{lang}', self.content_en) or self.content_en

    def __str__(self):
        return self.title_en