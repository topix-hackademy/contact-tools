from django.http import HttpResponse
from .models import Company
from .serializers_company import CompanySerializer
from .helper import auth_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q


def index(request):
    return HttpResponse("Control is an illusion")


@api_view(['GET', 'POST'])
@auth_decorator
def all_companies(request,format=None, *args, **kwargs):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        companies = Company.objects.all()
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
        
    company = Company.objects.filter(Q(company_vat_number__iexact=code) | Q( company_tax_code__iexact=code))[0]
    
    if company:
        if request.method == 'GET':
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET'])
@auth_decorator
def get_company_freesearch(request, searchstring, format=None):
    """
    Retrieve a company by free search
    """
    companies = Company.objects.filter( company_name__icontains=searchstring ).filter( company_short_name__icontains=searchstring ).filter( company_business_name__icontains=searchstring ).filter( company_website__icontains=searchstring ).filter( company_notes__icontains=searchstring ).all()

    if request.method == 'GET':
        serializer = CompanySerializer(companies, many=True,  remove_fields=['contacts'])
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


