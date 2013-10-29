from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.views import IndexView

admin.autodiscover()

#import core.admin

handler500 = 'core.views.server_error'

urlpatterns = patterns('', (r'^admin/doc/', include('django.contrib.admindocs.urls')), )

if 'grappelli' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', url(r'^grappelli/', include('grappelli.urls')), )

urlpatterns += patterns('', (r'^admin/', include(admin.site.urls)), )

urlpatterns += patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
)


urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        # Allows the 500.html page to be rendered in DEBUG mode
        (r'^500/$', 'core.views.server_error'),

    )