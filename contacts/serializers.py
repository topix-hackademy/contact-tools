from rest_framework import serializers
from .models import Company, CompanyType, Service, Contact, ContactType, CCRelation


class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = ('id','type_name', 'is_valid', 'creation_date')


class CompanySerializer(serializers.ModelSerializer):

    company_type = CompanyTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id','company_custom_id', 'company_name', 'company_short_name', 'company_business_name',
                  'company_vat_number', 'company_tax_code', 'company_address','company_cap','company_city',
                  'company_province','company_country', 'company_phone_number', 'company_fax', 'company_website',
                  'company_notes', 'creation_date', 'company_type')