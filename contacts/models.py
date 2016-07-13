from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime


def create_uid():
    import uuid
    return str(uuid.uuid4())


@python_2_unicode_compatible
class CompanyType(models.Model):

    type_name = models.CharField('Company Type', max_length=200)
    is_valid = models.BooleanField('Is Valid', default=True)
    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ('type_name',)


@python_2_unicode_compatible
class ContactType(models.Model):
    type_name = models.CharField('Contact Type', max_length=200)
    is_valid = models.BooleanField('Is Valid', default=True)
    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ('type_name',)


@python_2_unicode_compatible
class Company(models.Model):

    company_custom_id = models.IntegerField('Custom ID', null=False, unique=True)
    company_name = models.CharField('Company Name', max_length=200, null=False)
    company_short_name = models.CharField('Company Short Name', max_length=200, null=False)
    company_business_name = models.CharField('Company Business Name', max_length=200, null=False)
    company_vat_number = models.IntegerField('VAT Number', null=True, blank=True, unique=True)
    company_tax_code = models.IntegerField('Tax Code', null=True, blank=True, unique=True)
    company_address = models.CharField('Company Address', max_length=200, null=False)
    company_cap = models.CharField('CAP', max_length=10, null=False)
    company_city = models.CharField('City', max_length=200, null=False)
    company_province = models.CharField('Province', max_length=200, null=True, blank=True)
    company_country = models.CharField('Country', max_length=200, null=False)
    company_phone_number = models.CharField('Phone Number', max_length=100, null=True, blank=True)
    company_fax = models.CharField('FAX', max_length=200, null=True, blank=True)
    company_website = models.CharField('WebSite', max_length=200, null=True, blank=True)
    company_notes = models.TextField('Notes', null=True, blank=True)
    company_is_valid = models.BooleanField('Is Valid', default=True, null=False, blank=False)

    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)
    # Company Type relation
    company_type = models.ManyToManyField(CompanyType)

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ('company_name',)


@python_2_unicode_compatible
class Contact(models.Model):

    contact_username = models.CharField('Contact User Name', max_length=200, null=False, blank=False, unique=True)
    contact_first_name = models.CharField('Contact First Name', max_length=200, null=True, blank=True)
    contact_last_name = models.CharField('Contact Last Name', max_length=200, null=True, blank=True)
    contact_email = models.EmailField('Contact Email', max_length=200, null=False, blank=False)
    contact_phone = models.CharField('Contact Phone', max_length=100, null=True, blank=True)
    contact_notes = models.TextField('Notes', null=True, blank=True)

    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)

    def __str__(self):
        return self.contact_username + " - " + self.contact_email

    class Meta:
        ordering = ('contact_email',)


@python_2_unicode_compatible
class CCRelation(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)

    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)

    def __str__(self):
        return self.company.company_short_name + " - " + self.contact.contact_username \
               + " - " + self.contact_type.type_name


@python_2_unicode_compatible
class Service(models.Model):

    service_name = models.CharField('Service Name', max_length=200, null=False, blank=False)
    token = models.CharField('Token', default=create_uid, max_length=200, null=False, blank=False, unique=True)
    is_valid = models.BooleanField('Is Valid', default=True, null=False, blank=False)
    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)
    activation_date = models.DateTimeField('Activation Date', default=datetime.datetime.now)
    delete_date = models.DateTimeField('Delete Date', null=True, blank=True)
    notes = models.TextField('Notes', null=True, blank=True)


    def __str__(self):
        return self.service_name + " - " + self.token

    class Meta:
        ordering = ('service_name',)
