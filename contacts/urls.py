from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views_company, view_contact, view_role, view_company_type

urlpatterns = [

    url(r'^company-type/$', view_company_type.all_company_types),
    url(r'^company-type/(?P<id>[0-9]+)/$', view_company_type.single_company_type),

    url(r'^role/$', view_role.all_roles),
    url(r'^role/(?P<id>[0-9]+)/$', view_role.single_role),

    url(r'^contact/$', view_contact.all_contacts),
    url(r'^contact/(?P<id>[0-9]+)/$', view_contact.single_contact),

    url(r'^company/$', views_company.all_companies),
    url(r'^company/(?P<id>[0-9]+)/$', views_company.single_company),

    url(r'^$', views_company.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
