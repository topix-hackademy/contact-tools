from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.http import HttpResponse
import datetime
import json

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
                # obj.token = "INVALID"
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
    actions = ["export_companies"]
    fieldsets = [
        ('Company Info', 
            {'fields': ['company_name', 'company_short_name',
            'company_business_name', 'thumb_logo_display', 'company_logo', 'company_vat_number', 'company_tax_code']}),

        ('Contact Info', {'fields': ['company_phone_number', 'company_website', 'company_email', 'company_certified_email', 'company_fax' ]}),

        ('Notes', {'fields': ['company_notes']}),
        
        ('Company Type', {'fields': ['company_type']}),

        ('Main Address', {'fields': ['company_address', 'company_cap', 'company_city', 'company_province',
                                        'company_country']}),
        
        ('Mailing Address', {'fields': ['company_mailingaddress']}),
        
        
        ('External references', 
            {'fields': ['company_custom_id', 'company_centralservices_id']}),
        
    ]
    list_display = ('company_name', 'thumb_logo_display', 'display_types', 'company_city', 'company_website')
    search_fields = ['company_name', 'company_short_name', 'company_vat_number', 'company_tax_code']
    readonly_fields = ['thumb_logo_display']
    thumb_logo_display = AdminThumbnail(image_field='get_logo_or_default', template='admin/thumbnail.html')
    thumb_logo_display.short_description = "Company logo"
    inlines = [ RelationInline ]
    
    
    # override di changelist_view per permettere di eseguire l'azione su tutti gli oggetti
    # quando non ne viene selezionato alcuno nella lista
    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'export_companies':
            if not request.POST.getlist(ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in Company.objects.all():
                    post.update({ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(CompanyAdmin, self).changelist_view(request, extra_context)
    
    
    def export_companies(self, request, queryset):
        result=[]
        for item in queryset.all():
            company_types=[]
            for t in item.company_type.all():
                company_types.append(t.type_name)
            
            logo_image=""
            if item.company_logo and item.company_logo.path:
                logo_image = item.company_logo.path
            # quick and dirty serializer
            newitem={
                "id": item.id,
                "company_custom_id": item.company_custom_id,
                "company_name": item.company_name,
                "company_short_name": item.company_short_name,
                "company_business_name": item.company_business_name,
                "company_vat_number": item.company_vat_number,
                "company_tax_code": item.company_tax_code,
                "company_address": item.company_address,
                "company_cap": item.company_cap,
                "company_city": item.company_city,
                "company_province": item.company_province,
                "company_country": item.company_country,
                "company_mailingaddress": item.company_mailingaddress,
                "company_phone_number": item.company_phone_number,
                "company_fax": item.company_fax,
                "company_website": item.company_website,
                "company_notes": item.company_notes,
                "company_email": item.company_email,
                "company_certified_email": item.company_certified_email,
                "company_logo": logo_image,
                "company_type": company_types
            }
            result.append(newitem)
            
        content=json.dumps(result)
            
        response = HttpResponse(content, content_type='text/json')
        response['Content-Disposition'] = 'attachment; filename=company_records.json'
        return response
    
admin.site.register(Company, CompanyAdmin)


### CONTACT ADMIN

class ContactAdmin(admin.ModelAdmin):
    actions = ["export_contacts"]
    
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
    

    # override di changelist_view per permettere di eseguire l'azione su tutti gli oggetti
    # quando non ne viene selezionato alcuno nella lista
    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'export_contacts':
            if not request.POST.getlist(ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in Contact.objects.all():
                    post.update({ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(ContactAdmin, self).changelist_view(request, extra_context)
    
    
    def export_contacts(self, request, queryset):
        result=[]
        for item in queryset.all():
            company_relations=[]
            for r in item.ccrelation_set.all():
                company_relations.append({ "relation_type": r.contact_type.type_name, "company_id": r.company.id })
            
            # quick and dirty serializer
            newitem={
                "id": item.id,
                "contact_username": item.contact_username,
                "contact_first_name": item.contact_first_name,
                "contact_last_name": item.contact_last_name,
                "contact_email": item.contact_email,
                "contact_email_secondary": item.contact_email_secondary,
                "contact_phone": item.contact_phone,
                "contact_phone_secondary": item.contact_phone_secondary,
                "contact_notes": item.contact_notes,
                "company_relations": company_relations
            }
            result.append(newitem)
            
        content=json.dumps(result)
            
        response = HttpResponse(content, content_type='text/json')
        response['Content-Disposition'] = 'attachment; filename=contact_records.json'
        return response




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
