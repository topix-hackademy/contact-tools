from rest_framework import serializers
from .models import Contact, ContactType, Company, CCRelation
from .serializers_company import CompanyTypeSerializer


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = ('id','type_name', 'is_valid', 'creation_date')
        extra_kwargs = {'id': {'read_only': False}}


class ContactSerializer(serializers.ModelSerializer):

    role = serializers.DictField()

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(ContactSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)

    def create(self, validated_data):
        print validated_data
        contact_role_data = validated_data.pop('role')
        contact = Contact.objects.create(**validated_data)
        for item in contact_role_data['relations']:
            print item
            try:
                company = Company.objects.get(company_custom_id = item['company']['company_custom_id'])
                contact_type = ContactType.objects.get(type_name = item['role'])
                relationship = CCRelation.objects.create(company=company,contact_type=contact_type, contact = contact)
            except Exception as e:
                contact.delete()
                raise serializers.ValidationError({'company_type': ["Invalid company type"]})

            contact.save()
            relationship.save()
            return contact


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
                  'contact_phone', 'contact_notes', 'role')