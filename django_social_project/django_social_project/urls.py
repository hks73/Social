from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'django_social_app.views.login'),
    url(r'^home/$', 'django_social_app.views.home'),
    url(r'^logout/$', 'django_social_app.views.logout'),
    url(r'^blogs/$', 'django_social_app.views.blogs'),
    url(r'^getblogs/$', 'django_social_app.views.getBlogs'),
    url(r'^getblogs/(?P<bid>\d+)/$', 'django_social_app.views.addcomments'),
]
