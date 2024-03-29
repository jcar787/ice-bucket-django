from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ibs_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^army_navy_of_two/', include(admin.site.urls)),
    url(r'', include('participants.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
