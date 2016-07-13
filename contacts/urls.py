from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from . import company_views, contact_view

urlpatterns = [
    url(r'^contact/$', contact_view.all_contacts),
    url(r'^contact/(?P<id>[0-9]+)/$', contact_view.single_contact),
    url(r'^company/$', company_views.all_companies),
    url(r'^company/(?P<id>[0-9]+)/$', company_views.single_company),
    url(r'^$', company_views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)