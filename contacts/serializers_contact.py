from rest_framework import serializers
from .models import Contact, ContactType
from .serializers_company import CompanySerializer


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = ('id','type_name', 'is_valid', 'creation_date')
        extra_kwargs = {'id': {'read_only': False}}


class ContactSerializer(serializers.ModelSerializer):

    contact_company = CompanySerializer(many=True)

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(ContactSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)

    # def create(self, validated_data):
    #     company_type_data = validated_data.pop('company_type')
    #     contact = Contact.objects.create(**validated_data)
    #
    #     for item in company_type_data:
    #         try:
    #             company_type = CompanyType.objects.get(id=item['id'])
    #         except Exception as e:
    #             company.delete()
    #             raise serializers.ValidationError({'company_type': ["Invalid company type"]})
    #         company.company_type.add(company_type)
    #     company.save()
    #     return company

    # def update(self,  instance, validated_data):
    #     company_type_data = validated_data.pop('company_type')
    #
    #     instance.company_name = validated_data.get('company_name', instance.company_name)
    #     instance.company_short_name = validated_data.get('company_short_name', instance.company_short_name)
    #     instance.company_business_name = validated_data.get('company_business_name', instance.company_business_name)
    #     instance.company_vat_number = validated_data.get('company_vat_number', instance.company_vat_number)
    #     instance.company_tax_code = validated_data.get('company_tax_code', instance.company_tax_code)
    #     instance.company_address = validated_data.get('company_address', instance.company_address)
    #     instance.company_cap = validated_data.get('company_cap', instance.company_cap)
    #     instance.company_city = validated_data.get('company_city', instance.company_city)
    #     instance.company_province = validated_data.get('company_province', instance.company_province)
    #     instance.company_country = validated_data.get('company_country', instance.company_country)
    #     instance.company_phone_number = validated_data.get('company_phone_number', instance.company_phone_number)
    #     instance.company_fax = validated_data.get('company_fax', instance.company_fax)
    #     instance.company_website = validated_data.get('company_website', instance.company_website)
    #     instance.company_notes = validated_data.get('company_notes', instance.company_notes)
    #     instance.company_type.clear()
    #     for item in company_type_data:
    #         try:
    #             company_type = CompanyType.objects.get(id=item['id'])
    #         except Exception as e:
    #             raise serializers.ValidationError({'company_type': ["Invalid company type"]})
    #         instance.company_type.add(company_type)
    #     instance.save()
    #     return instance



    class Meta:
        model = Contact
        fields = ('id', 'contact_username', 'contact_first_name', 'contact_last_name', 'contact_email',
                  'contact_phone', 'contact_notes', 'contact_company')