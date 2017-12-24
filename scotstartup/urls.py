from django.conf.urls import patterns, url
from scotstartup import views
from scotstartup import forms

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^search/$', views.search, name='search'),
        url(r'^about/$', views.about, name='about'),
        url(r'^news/$', views.news, name='news'),
        url(r'^add_company/$', views.add_company, name="add_company"),
        url(r'^add_event/$', views.add_event, name="add_event"),
        url(r'^event/(?P<event_name_slug>[\w\-]+)/$', views.event, name="event"),
        url(r'^events/$', views.events, name="events"),
        url(r'^company/(?P<company_name_slug>[\w\-]+)/$', views.company, name="company"),
        url(r'^companies/$', views.companies, name="companies"),)

