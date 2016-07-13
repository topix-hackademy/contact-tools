from django.http import HttpResponse
from .models import Contact
from .contact_serializers import ContactSerializer
from .helper import auth_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
@auth_decorator
def all_contacts(request,format=None, *args, **kwargs):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
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
        company = Company.objects.get(company_custom_id=id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        return Response(status=status.HTTP_400_BAD_REQUEST)