from .models import Contact, CCRelation
from .serializers_contact import ContactSerializer, RelationSerializer
from .helper import auth_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import Q

import logging
logger = logging.getLogger('ct-logger')


@api_view(['GET','POST'])
@auth_decorator
def all_contacts(request,format=None, *args, **kwargs):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True, remove_fields=['role'])
        return Response(serializer.data)

    elif request.method == 'POST':
        logger.debug("going to create contact")
        logger.debug(request.data)
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@auth_decorator
def single_contact(request, id, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    logger.debug("entering single_contact, method " + request.method)
    try:
        contact = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
	logger.debug("going to update contact")
        if serializer.is_valid():
	    logger.debug("data is valid")
            serializer.save()
	    logger.debug("data saved")
            return Response(serializer.data)
	logger.debug("data is not valid")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@auth_decorator
def get_contact_by_email(request, email, format=None):
    """
    Retrieve a contact by email address
    """
    try:
        contact = Contact.objects.filter(Q(contact_email=email) | Q(contact_email_secondary=email))
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@auth_decorator
def get_contact_by_username(request, username, format=None):
    """
    Retrieve a contact by username
    """
    try:
        contact = Contact.objects.filter(contact_username=username)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@auth_decorator
def get_contact_by_csid(request, csid, format=None):
    """
    Retrieve a contact by Centralservices ID
    """
    contacts = Contact.objects.filter(contact_centralservices_id=csid).all()

    if request.method == 'GET':
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@auth_decorator
def all_relations(request,format=None, *args, **kwargs):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        relations = CCRelation.objects.all()
        serializer = RelationSerializer(relations, many=True)
        return Response(serializer.data)
