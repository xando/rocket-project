from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns(
  '',
  url(r'^$', 'test.views.index', name='home'),
  url(r'^media/(?P<blobstore_key>.*)$','rocket_engine.views.file_serve'),
)
