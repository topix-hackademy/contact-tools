from rest_framework import serializers
from .models import Company, CompanyType


class CompanyTypeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        company_type = CompanyType.objects.create(**validated_data)
        company_type.save()
        return company_type

    def update(self, instance, validated_data):
        instance.type_name = validated_data.get('type_name', instance.type_name)
        instance.is_valid = validated_data.get('is_valid', instance.is_valid)
        instance.save()
        return instance

    class Meta:
        model = CompanyType
        fields = ('id', 'type_name', 'is_valid', 'creation_date')
        extra_kwargs = {'id': {'read_only': True}}


class CompanyTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = ('id', 'type_name', 'is_valid', 'creation_date')
        extra_kwargs = {'id': {'read_only': False}}


class CompanySerializer(serializers.ModelSerializer):

    company_type = CompanyTypeReadSerializer(many=True)
    contacts = serializers.ReadOnlyField()

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(CompanySerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)

    def create(self, validated_data):
        company_type_data = validated_data.pop('company_type')
        company = Company.objects.create(**validated_data)
        for item in company_type_data:
            try:
                company_type = CompanyType.objects.get(id=item['id'])
            except:
                company.delete()
                raise serializers.ValidationError({'company_type': ["Invalid company type"]})
            company.company_type.add(company_type)
        company.save()
        return company

    def update(self, instance, validated_data):
        company_type_data = validated_data.pop('company_type')

        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_short_name = validated_data.get('company_short_name', instance.company_short_name)
        instance.company_business_name = validated_data.get('company_business_name', instance.company_business_name)
        instance.company_vat_number = validated_data.get('company_vat_number', instance.company_vat_number)
        instance.company_tax_code = validated_data.get('company_tax_code', instance.company_tax_code)
        instance.company_address = validated_data.get('company_address', instance.company_address)
        instance.company_cap = validated_data.get('company_cap', instance.company_cap)
        instance.company_city = validated_data.get('company_city', instance.company_city)
        instance.company_province = validated_data.get('company_province', instance.company_province)
        instance.company_country = validated_data.get('company_country', instance.company_country)
        instance.company_mailingaddress = validated_data.get('company_mailingaddress', instance.company_mailingaddress)
        instance.company_phone_number = validated_data.get('company_phone_number', instance.company_phone_number)
        instance.company_fax = validated_data.get('company_fax', instance.company_fax)
        instance.company_website = validated_data.get('company_website', instance.company_website)
        instance.company_notes = validated_data.get('company_notes', instance.company_notes)
        instance.company_logo = validated_data.get('company_logo', instance.company_logo.get_absolute_url())
        instance.company_type.clear()
        for item in company_type_data:
            try:
                company_type = CompanyType.objects.get(id=item['id'])
            except:
                raise serializers.ValidationError({'company_type': ["Invalid company type"]})
            instance.company_type.add(company_type)
        instance.save()
        return instance

    class Meta:
        model = Company
        fields = ('id', 'company_custom_id', 'company_name', 'company_logo', 'company_short_name', 'company_business_name',
                  'company_vat_number', 'company_tax_code', 'company_address', 'company_cap', 'company_city',
                  'company_province', 'company_country', 'company_mailingaddress', 'company_phone_number', 'company_fax', 'company_website',
                  'company_notes', 'creation_date', 'company_type', 'contacts')
