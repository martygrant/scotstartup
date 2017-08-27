from django.conf.urls import patterns, url
from scotstartup import views
from scotstartup import forms

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_company/$', views.add_company, name="add_company"),
        url(r'^company/(?P<company_name_slug>[\w\-]+)/$', views.company, name="company"),)

