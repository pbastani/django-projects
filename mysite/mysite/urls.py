from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^portfolio/', include('portfolio.urls', namespace="portfolio", app_name="portfolio")),
                       url(r'^timeline/', include('timeline.urls', namespace="timeline")),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^picit/', include('picit.urls', namespace="picit")),
                       url(r'^admin/', include(admin.site.urls)),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)