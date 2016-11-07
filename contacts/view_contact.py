from .models import Contact
from .serializers_contact import ContactSerializer
from .helper import auth_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

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
    try:
        contact = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@auth_decorator
def get_contact_by_email(request, email, format=None):
    """
    Retrieve a company by email address
    """
    try:
        contact = Contact.objects.filter(contact_email=email)
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
    contacts = Contact.objects.filter( contact_centralservices_id=csid ).all()

    if request.method == 'GET':
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

