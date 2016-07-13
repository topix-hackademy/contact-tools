from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from . import views_company, view_contact

urlpatterns = [
    url(r'^contact/$', view_contact.all_contacts),
    url(r'^contact/(?P<id>[0-9]+)/$', view_contact.single_contact),
    url(r'^company/$', views_company.all_companies),
    url(r'^company/(?P<id>[0-9]+)/$', views_company.single_company),
    url(r'^$', views_company.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)