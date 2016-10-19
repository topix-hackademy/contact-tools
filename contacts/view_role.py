from django.http import HttpResponse
from .models import ContactType
from .serializers_contact import ContactTypeSerializer
from .helper import auth_decorator, response_404, response_400
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import logging
logger = logging.getLogger('ct-logger')


@api_view(['GET','POST'])
@auth_decorator
def all_roles(request,format=None, *args, **kwargs):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        roles = ContactType.objects.all()
        serializer = ContactTypeSerializer(roles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@auth_decorator
def single_role(request, id, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        role = ContactType.objects.get(id=id)
    except ContactType.DoesNotExist:
        return response_404()

    if request.method == 'GET':
        serializer = ContactTypeSerializer(role)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactTypeSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        return response_400()