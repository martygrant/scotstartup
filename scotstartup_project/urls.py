from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/scotstartup/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scotstartup_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^scotstartup/', include('scotstartup.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name="registration_register"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
