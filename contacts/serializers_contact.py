from rest_framework import serializers
from .models import Contact, ContactType, Company, CCRelation
from .serializers_company import CompanyTypeSerializer


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = ('id', 'type_name', 'is_valid', 'creation_date')
        extra_kwargs = {'id': {'read_only': False}}


class ContactSerializer(serializers.ModelSerializer):

    role = serializers.DictField()

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(ContactSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)

    def create(self, validated_data):
        print validated_data
        contact_role_data = validated_data.pop('role')
        contact = Contact.objects.create(**validated_data)
        for item in contact_role_data['relations']:
            print item
            try:
                company = Company.objects.get(company_custom_id=item['company']['company_custom_id'])
                contact_type = ContactType.objects.get(type_name=item['role'])
                relationship = CCRelation.objects.create(company=company, contact_type=contact_type, contact=contact)
            except Exception as e:
                contact.delete()
                raise serializers.ValidationError({'company_type': ["Invalid role"]})

            contact.save()
            relationship.save()
            return contact

    def update(self,  instance, validated_data):

        contact_role_data = validated_data.pop('role')

        instance.contact_username = validated_data.get('contact_username', instance.contact_username)
        instance.contact_first_name = validated_data.get('contact_first_name', instance.contact_first_name)
        instance.contact_last_name = validated_data.get('contact_last_name', instance.contact_last_name)
        instance.contact_email = validated_data.get('contact_email', instance.contact_email)
        instance.contact_phone = validated_data.get('contact_phone', instance.contact_phone)
        instance.contact_notes = validated_data.get('contact_notes', instance.contact_notes)

        for item in contact_role_data['relations']:
            try:
                relationship = CCRelation.objects.filter(company__company_custom_id=item['company']['company_custom_id'], contact_type__type_name=item['role'], contact=instance)
                if not relationship:
                    try:
                        company = Company.objects.get(company_custom_id=item['company']['company_custom_id'])
                        contact_type = ContactType.objects.get(type_name=item['role'])
                        CCRelation.objects.create(company=company, contact_type=contact_type, contact=instance)
                    except Exception as e:
                        raise serializers.ValidationError({'Validation Error': ["Invalid company and/or invalid contact_type"]})
            except Exception as e:
                raise serializers.ValidationError({'Validation Error': ["Invalid company and/or invalid contact_type"]})
        instance.save()
        return instance

    class Meta:
        model = Contact
        fields = ('id', 'contact_username', 'contact_first_name', 'contact_last_name', 'contact_email',
                  'contact_phone', 'contact_notes', 'role')