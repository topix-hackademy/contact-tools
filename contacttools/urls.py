from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='Index'),
    url(r'^api/v1/', include('contacts.urls')),
    url(r'^admin/', admin.site.urls),
]
