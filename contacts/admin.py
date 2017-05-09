from django.contrib import admin
import datetime

from imagekit.admin import AdminThumbnail

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

class RelationInline(admin.TabularInline):
    model = CCRelation
    # fk_name = 'device'
    exclude = [ ]
    readonly_fields = ['company', 'contact', 'contact_type']
    extra=0


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Info', 
            {'fields': ['company_name', 'company_short_name',
            'company_business_name', 'thumb_logo_display', 'company_logo', 'company_vat_number', 'company_tax_code']}),

        ('Notes', {'fields': ['company_notes']}),
        
        ('Company Type', {'fields': ['company_type']}),

        ('Main Address', {'fields': ['company_address', 'company_cap', 'company_city', 'company_province',
                                        'company_country']}),
        
        ('Mailing Address', {'fields': ['company_mailingaddress']}),
        
        ('Contact Info', {'fields': ['company_phone_number', 'company_fax', 'company_website']}),
        
        ('External references', 
            {'fields': ['company_custom_id', 'company_centralservices_id']}),
        
    ]
    list_display = ('company_name', 'thumb_logo_display', 'display_types', 'company_city', 'company_website')
    search_fields = ['company_name', 'company_short_name', 'company_vat_number', 'company_tax_code']
    readonly_fields = ['thumb_logo_display']
    thumb_logo_display = AdminThumbnail(image_field='get_logo_or_default', template='admin/thumbnail.html')
    thumb_logo_display.short_description = "Company logo"
    inlines = [ RelationInline ]
    
admin.site.register(Company, CompanyAdmin)


### CONTACT ADMIN

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Contact Info', {'fields': ['contact_username', 'contact_first_name', 'contact_last_name']}),
        ('Contact Address', {'fields': ['contact_email', 'contact_email_secondary', 'contact_phone', 'contact_phone_secondary']}),
        ('Notes', {'fields': ['contact_notes']}),
        ('External references', 
            {'fields': ['contact_centralservices_id']}),
        
    ]
    list_display = ('contact_first_name', 'contact_last_name', 'contact_email', 'contact_username')
    search_fields = ['contact_username', 'contact_email', 'contact_last_name', 'contact_first_name']
    inlines = [ RelationInline ]
    

admin.site.register(Contact, ContactAdmin)

## CC RELATION ADMIN

class CCRelationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CC Relation', {'fields': ['company', 'contact', 'contact_type']})
    ]
    list_display = ('company', 'contact', 'contact_type')
    list_filter = ['contact_type']
    search_fields = ['company__company_name', 'contact__contact_first_name', 'contact__contact_last_name', 'contact__contact_email', 'contact__contact_username']

admin.site.register(CCRelation, CCRelationAdmin)
