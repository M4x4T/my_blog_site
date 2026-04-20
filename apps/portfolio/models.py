from django.db import models
from django.utils.translation import get_language

class Project(models.Model):
    # Technical Metadata (Language Independent)
    tools_used = models.CharField(max_length=200, help_text="e.g. Python, Scikit-Learn")
    github_url = models.URLField(blank=True)
    notebook_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Language Specific Fields
    title_en = models.CharField(max_length=200)
    description_en = models.TextField()

    title_tr = models.CharField(max_length=200, blank=True)
    description_tr = models.TextField(blank=True)

    title_ru = models.CharField(max_length=200, blank=True)
    description_ru = models.TextField(blank=True)

    def __str__(self):
        return self.title_en

    @property
    def translated_title(self):
        lang = get_language()
        # Returns the requested language, or falls back to English
        return getattr(self, f'title_{lang}', self.title_en) or self.title_en

    @property
    def translated_description(self):
        lang = get_language()
        return getattr(self, f'description_{lang}', self.description_en) or self.description_en