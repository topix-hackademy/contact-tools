from django.contrib import admin

## My Models
from .models import CompanyType, Service

class CompanyTypeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Company Type', {'fields': ['type_name', 'is_valid']}),
    ]
    list_display = ('type_name', 'is_valid', 'creation_date')
    list_filter = ['creation_date', 'is_valid']
    search_fields = ['type_name']


admin.site.register(CompanyType, CompanyTypeAdmin)


class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Service Info', {'fields': ['service_name', 'is_valid']}),
        ('Token Management', {'fields': ['token']}),
        ('Notes', {'fields': ['notes']})
    ]
    list_display = ('service_name', 'token','is_valid', 'creation_date', 'activation_date', 'delete_date')
    list_filter = ['creation_date', 'is_valid']
    search_fields = ['service_name']

admin.site.register(Service, ServiceAdmin)

