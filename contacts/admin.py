from django.contrib import admin
import datetime

## My Models
from .models import CompanyType, Service, Company, Contact, ContactType, CCRelation

### COMPANY TYPE ADMIN

class CompanyTypeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Company Type', {'fields': ['type_name', 'is_valid']}),
    ]
    list_display = ('type_name', 'is_valid', 'creation_date')
    list_filter = ['creation_date', 'is_valid']
    search_fields = ['type_name']


admin.site.register(CompanyType, CompanyTypeAdmin)

### CONTACT TYPE ADMIN

class ContactTypeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Contact Type', {'fields': ['type_name', 'is_valid']}),
    ]
    list_display = ('type_name', 'is_valid', 'creation_date')
    list_filter = ['creation_date', 'is_valid']
    search_fields = ['type_name']


admin.site.register(ContactType, ContactTypeAdmin)

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

### COMPANY ADMIN

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Info', {'fields': ['company_custom_id', 'company_name', 'company_short_name',
                                     'company_business_name', 'company_vat_number', 'company_tax_code']}),
        ('Company Address', {'fields': ['company_address', 'company_cap', 'company_city', 'company_province',
                                        'company_country']}),
        ('Company Contacs', {'fields': ['company_phone_number', 'company_fax', 'company_website']}),
        ('Company Type', {'fields': ['company_type']}),
        ('Notes', {'fields': ['company_notes']})
    ]
    list_display = ('company_name', 'company_short_name', 'company_custom_id', 'company_vat_number', 'company_tax_code')
    search_fields = ['company_name', 'company_short_name', 'company_vat_number', 'company_tax_code']

admin.site.register(Company, CompanyAdmin)


### CONTACT ADMIN

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Contact Info', {'fields': ['contact_username', 'contact_first_name', 'contact_last_name']}),
        ('Contact Address', {'fields': ['contact_email', 'contact_phone']}),
        ('Notes', {'fields': ['contact_notes']})
    ]
    list_display = ('contact_username', 'contact_email', 'contact_first_name', 'contact_last_name')
    search_fields = ['contact_username', 'contact_email', 'contact_last_name']


admin.site.register(Contact, ContactAdmin)

## CC RELATION ADMIN

class CCRelationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CC Relation', {'fields': ['company', 'contact', 'contact_type']})
    ]
    list_display = ('company', 'contact', 'contact_type')
    list_filter = ['contact_type']
    search_fields = ['company', 'contact']

admin.site.register(CCRelation, CCRelationAdmin)
