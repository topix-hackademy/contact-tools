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
    url(r'^contact-by-csid/(?P<csid>[0-9]+)/$', view_contact.get_contact_by_csid),

    url(r'^company/$', views_company.all_companies),
    url(r'^company/(?P<id>[0-9]+)/$', views_company.single_company),

    url(r'^contact-by-email/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', view_contact.get_contact_by_email),
    url(r'^contact-by-username/(?P<username>[\w\s]+)/$', view_contact.get_contact_by_username),

    url(r'^company-by-code/(?P<code>\w{0,50})/$', views_company.get_company_by_code),
    url(r'^company-by-csid/(?P<csid>[0-9]+)/$', views_company.get_company_by_csid),
    url(r'^company-freesearch/(?P<searchstring>[\w\s]+)/$', views_company.get_company_freesearch),

    url(r'^relation/$', view_contact.all_relations),

    url(r'^$', views_company.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
