from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'forum.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r"^profile/(?P<pk>)\d+/$", 'forum.views.profile', name="profile"),
    url(r'^register/', 'forum.views.register'),
    url(r'^logout/', 'forum.views.logout_view'),
    url(r'^login/', 'forum.views.login_view'),
    url(r"^new-thread/(?P<pk>\d+)/$", 'forum.views.new_thread', name="new_thread"),
    url(r"^threads/(?P<pk>\d+)/$", 'forum.views.list_thread', name="list_thread"),
    url(r"^post/(?P<pk>\d+)/$", 'forum.views.list_post', name="list_post"),
    url(r"^reply/(?P<pk>\d+)/$", 'forum.views.new_reply', name="new_reply"),
)
