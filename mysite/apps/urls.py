from django.conf.urls import patterns,url
from django.conf import settings

urlpatterns = patterns('mysite.apps.views',
	url(r'^$','index_view',name='index'),
	url(r'^menuA/$','menuA_view',name='menuA'),
	url(r'^menue/$','menuE_view',name='menuE'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)