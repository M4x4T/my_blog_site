from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView
from apps.pages.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', RedirectView.as_view(url='/en/', permanent=False)), 
]

urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('articles/', include('apps.blog.urls')),
    path('portfolio/', include('apps.portfolio.urls')),
    prefix_default_language=True,
)