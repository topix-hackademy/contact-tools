from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

urlpatterns = [
    url(r'^company/$', views.all_companies),
    url(r'^company/(?P<id>[0-9]+)/$', views.single_company),
    url(r'^$', views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)