from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'mattespill.main.views.index'),
	(r'^questions/(?P<question_id>\d+)/$', 'mattespill.main.views.questions'),
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', 'mattespill.main.views.logout'),
	(r'^room/(?P<room_id>\d+)/$', 'mattespill.main.views.room'),

	# Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),

	# Hack to server static files
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
)
