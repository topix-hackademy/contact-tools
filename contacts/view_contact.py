from .models import Contact
from .serializers_contact import ContactSerializer
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
        serializer = ContactSerializer(contacts, many=True, remove_fields=['role'])
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