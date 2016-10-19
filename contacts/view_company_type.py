from django.http import HttpResponse
from .models import CompanyType
from .serializers_company import CompanyTypeSerializer
from .helper import auth_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import logging
logger = logging.getLogger('ct-logger')


@api_view(['GET', 'POST'])
@auth_decorator
def all_company_types(request, format=None, *args, **kwargs):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        company_types = CompanyType.objects.all()
        serializer = CompanyTypeSerializer(company_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanyTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@auth_decorator
def single_company_type(request, id, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        company_type = CompanyType.objects.get(id=id)
    except CompanyType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanyTypeSerializer(company_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanyTypeSerializer(company_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        return Response(status=status.HTTP_400_BAD_REQUEST)
