from rest_framework import serializers
from .models import Contact, ContactType, Company, CCRelation
from .helper import return_oldvalue_if_empty

import logging
logger = logging.getLogger('ct-logger')


class ContactTypeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        contact_role = ContactType.objects.create(**validated_data)
        contact_role.save()
        return contact_role

    def update(self, instance, validated_data):
        instance.type_name = validated_data.get('type_name', instance.type_name)
        instance.is_valid = validated_data.get('is_valid', instance.is_valid)
        instance.save()
        return instance

    class Meta:
        model = ContactType
        fields = ('id', 'type_name', 'is_valid', 'creation_date')
        extra_kwargs = {'id': {'read_only': True}}


class ContactSerializer(serializers.ModelSerializer):

    role = serializers.DictField()

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(ContactSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)

    def create(self, validated_data):
        contact_role_data = validated_data.pop('role')
        contact = Contact.objects.create(**validated_data)
        for item in contact_role_data['relations']:
            try:
                company = Company.objects.get(id=item['company']['id'])
                contact_type = ContactType.objects.get(type_name=item['role'])
                relationship = CCRelation.objects.create(company=company, contact_type=contact_type, contact=contact)
            except Exception as e:
                print e
                contact.delete()
                raise serializers.ValidationError({'contact_type': ["Invalid role"]})

            contact.save()
            relationship.save()
            return contact

    def update(self,  instance, validated_data):
        contact_role_data = validated_data.pop('role')

        instance.contact_username = return_oldvalue_if_empty(validated_data.get('contact_username', ""),
                                                             instance.contact_username)
        instance.contact_first_name = return_oldvalue_if_empty(validated_data.get('contact_first_name', ""),
                                                               instance.contact_first_name)
        instance.contact_last_name = return_oldvalue_if_empty(validated_data.get('contact_last_name', ""),
                                                              instance.contact_last_name)
        instance.contact_email = return_oldvalue_if_empty(validated_data.get('contact_email', ""),
                                                          instance.contact_email)
        instance.contact_email_secondary = return_oldvalue_if_empty(validated_data.get('contact_email_secondary', ""),
                                                                    instance.contact_email_secondary)
        instance.contact_phone = return_oldvalue_if_empty(validated_data.get('contact_phone', ""),
                                                          instance.contact_phone)
        instance.contact_phone_secondary = return_oldvalue_if_empty(validated_data.get('contact_phone_secondary', ""),
                                                                    instance.contact_phone_secondary)
        instance.contact_notes = return_oldvalue_if_empty(validated_data.get('contact_notes', ""),
                                                          instance.contact_notes)


        # compare existing relationships for this contact with the relationships provided
        relations_db=CCRelation.objects.filter(contact=instance)
        
        auditresult=auditRelations(relations_db, contact_role_data['relations'])
        
        for res in auditresult:
            localRel=res['loc']
            remoteRel=res['rem']
            
            if localRel:
                
                if remoteRel:
                    # relation is present both in the local and remote lists
                    # nothing to do
                    pass
                else:
                    # relation is present in the local lists but not in the remote list
                    # remove the relation
                    #logger.info("removing relation " + localRel.company.company_name +" (" +localRel.contact_type.type_name+ ")")
                    localRel.delete()
    
            elif remoteRel:
                # relation is present only in the remote list
                #logger.info("adding relation " + remoteRel["company"]["company_name"] +" (" +remoteRel["role"]+ ")")
                try:
                    contact_type = ContactType.objects.get(type_name=remoteRel['role'])
                    company = Company.objects.get(id=remoteRel['company']['id'])
                    CCRelation.objects.create(company=company, contact_type=contact_type, contact=instance)
                except Exception as e:
                    print e
                    raise serializers.ValidationError({'Validation Error': ["Invalid company and/or invalid contact_type"]})
        
        
        
        '''
        for item in contact_role_data['relations']:
            try:
                contact_type = ContactType.objects.get(type_name=item['role'])
                relationship = CCRelation.objects.filter(company__id=item['company']['id'], contact=instance)
                company = Company.objects.get(id=item['company']['id'])
                if relationship:
                    relationship.delete()
                CCRelation.objects.create(company=company, contact_type=contact_type, contact=instance)

            except Exception as e:
                print e
                raise serializers.ValidationError({'Validation Error': ["Invalid company and/or invalid contact_type"]})
        '''
        
        
        instance.save()
        return instance

    class Meta:
        model = Contact
        fields = ('id', 'contact_username', 'contact_first_name', 'contact_last_name', 'contact_email', 'contact_email_secondary',
                  'contact_phone', 'contact_phone_secondary', 'contact_notes', 'role', 'contact_centralservices_id')


class MiniCompamySerializer(serializers.ModelSerializer):
    
    class Meta:
        model: Company
        fields = ('id', 'company_name')
        extra_kwargs = {'id': {'read_only': True}}

class RelationSerializer(serializers.ModelSerializer):
    company = MiniCompamySerializer()
    contact = ContactSerializer()
    contact_type = ContactTypeSerializer()
    
    
    class Meta:
        model: CCRelation
        fields = ('id', 'company', 'contact', 'contact_type')
        extra_kwargs = {'id': {'read_only': True}}



def auditRelations(localObjects, remoteObjects):
    result = []

    foundRemoteObjRef = []
    
    remoteObjects_nodupe=[]
    # remove duplicates
    for remobj in remoteObjects:
        if not remobj in remoteObjects_nodupe:
            remoteObjects_nodupe.append(remobj)

    # iterate through the relations in the local DB
    for locobj in localObjects:
        # use the pair company id and role name to find matches
        localRefFieldValue="%d-%s" % (locobj.company.id, locobj.contact_type.type_name)
        
        remObjFound = None
        for remobj in remoteObjects_nodupe:
            crossref="%d-%s" % (remobj["company"]["id"], remobj["role"])

            if crossref == localRefFieldValue:
                remObjFound=remobj
                foundRemoteObjRef.append(crossref)

                break

        if remObjFound == None:
            # relation is in the local DB and not in the remote list
            res={'loc': locobj, 'rem': None}
        else:
            # relation is in both remote and local lists
            res={'loc': locobj, 'rem': remObjFound}


        result.append(res)


    # find relations that are in the remote list but are not in the DB
    for remobj in remoteObjects:
        crossref="%d-%s" % (remobj["company"]["id"], remobj["role"])

        if crossref not in foundRemoteObjRef:
            # the relation in the remote list is not in the DB
            # hence it needs to be created
            res={'loc': None, 'rem': remobj}
            result.append(res)


    return result
    

