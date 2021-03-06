from django.http import HttpResponse

from .models import Company, CompanyType
from .serializers_company import CompanySerializer
from .helper import auth_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q

import logging
logger = logging.getLogger('ct-logger')


def index(request):
    return HttpResponse("Control is an illusion")


@api_view(['GET', 'POST'])
@auth_decorator
def all_companies(request,format=None, *args, **kwargs):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        query=Q()
        # check if a filter is provided
        if 'types' in request.GET and request.GET['types'] and request.GET['types'] != '':
            type_names=request.GET['types'].split(',')
            
            for typename in type_names:
                query = query | Q(company_type__type_name=typename)
        
        companies = Company.objects.filter(query).all()
        serializer = CompanySerializer(companies, many=True,  remove_fields=['contacts'])
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@auth_decorator
def single_company(request, id, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        company = Company.objects.get(id=id)
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


@api_view(['GET'])
@auth_decorator
def get_company_by_code(request, code, format=None):
    """
    Retrieve a company by code (first match is returned)
    """
        
    company = Company.objects.filter(Q(company_vat_number__iexact=code) | Q( company_tax_code__iexact=code)).first()
    
    if company:
        if request.method == 'GET':
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        print("company not found")
        company = Company.objects.filter(
            Q(company_vat_number__iendswith=code) | Q(company_tax_code__iendswith=code)).first()
        if company:
            if request.method == 'GET':
                serializer = CompanySerializer(company)
                return Response(serializer.data)
        else:
            print("company not found 2")
            return Response(status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET'])
@auth_decorator
def get_company_by_csid(request, csid, format=None):
    """
    Retrieve a company by Centralservices ID
    """
    companies = Company.objects.filter( company_centralservices_id=csid ).all()

    if request.method == 'GET':
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@auth_decorator
def get_company_freesearch(request, searchstring, format=None):
    """
    Retrieve a company by free search
    """
    companies = Company.objects.filter( Q(company_name__icontains=searchstring) | Q(company_short_name__icontains=searchstring) | Q(company_business_name__icontains=searchstring) | Q(company_website__icontains=searchstring) | Q(company_notes__icontains=searchstring) ).all()

    if request.method == 'GET':
        serializer = CompanySerializer(companies, many=True,  remove_fields=['contacts'])
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


