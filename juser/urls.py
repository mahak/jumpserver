from django.conf.urls import patterns, include, url


urlpatterns = patterns('juser.views',
    # Examples:
    # url(r'^$', 'jumpserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^useradd/$', 'user_add'),
)