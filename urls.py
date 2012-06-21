from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns(
  '',
  url(r'^$', 'core.views.index', name='home'),
  url(r'^media/(?P<filename>.*)$','rocket_engine.views.file_serve'),
)
