from django.contrib import admin
import datetime

## My Models
from .models import CompanyType, Service

### COMPANY TYPE ADMIN

class CompanyTypeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Company Type', {'fields': ['type_name', 'is_valid']}),
    ]
    list_display = ('type_name', 'is_valid', 'creation_date')
    list_filter = ['creation_date', 'is_valid']
    search_fields = ['type_name']


admin.site.register(CompanyType, CompanyTypeAdmin)

### SERVICE ADMIN

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Service Info', {'fields': ['service_name', 'is_valid']}),
        ('Token Management', {'fields': ['token']}),
        ('Notes', {'fields': ['notes']})
    ]
    list_display = ('service_name', 'token','is_valid', 'creation_date', 'activation_date', 'delete_date')
    list_filter = ['creation_date', 'is_valid']
    search_fields = ['service_name']


    def save_model(self, request, obj, form, change):
        if change:
            old_obj = Service.objects.get(id=obj.id)
            if old_obj.is_valid and not obj.is_valid:
                # set service not valid
                obj.delete_date = datetime.datetime.now()
                obj.token = "INVALID"
            elif not old_obj.is_valid and obj.is_valid:
                # set service valid
                obj.delete_date = None
                obj.activation_date = datetime.datetime.now()
        obj.save()

admin.site.register(Service, ServiceAdmin)

