from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import get_language
from django.shortcuts import redirect
from apps.pages.views import home

def root_redirect(request):
    lang = get_language() or 'en'
    return redirect(f'/{lang}/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', root_redirect),  # ← reads the cookie and redirects correctly
]

urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('articles/', include('apps.blog.urls')),
    path('portfolio/', include('apps.portfolio.urls')),
    prefix_default_language=True,
)