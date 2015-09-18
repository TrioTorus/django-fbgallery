from django.conf.urls import patterns
from django.conf import settings

fb_id = getattr(settings, 'FB_PAGE_ID', None)

urlpatterns = patterns(
    'fbgallery.views',
    (r'^$', 'display_albums', {'fb_id': fb_id}, 'fb-albums'),
    (r'^(?P<album_id>[-\w]+)/$', 'display_album', {'fb_id': fb_id}, 'fb-album'),
)
