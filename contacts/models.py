from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError

import datetime

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

import os
from django.dispatch import receiver
import logging
logger = logging.getLogger('ct-logger')


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
    type_name = models.CharField('Contact Type', max_length=200, unique=True)
    is_valid = models.BooleanField('Is Valid', default=True)
    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ('type_name',)


@python_2_unicode_compatible
class Company(models.Model):
    DEFAULT_LOGO_FILE = 'logos/nologo.png'
    
    # this is needed to sync with the old CS
    company_centralservices_id = models.IntegerField('Old Centralservices ID', null=True, blank=True, help_text="ID of this Company in the old CS")
    
    company_custom_id = models.IntegerField('Custom External ID', null=True, blank=True, help_text="ID of this Company in external systems (eg. ESolver)")
    company_name = models.CharField('Company Name', max_length=200, null=False, blank=False)
    company_short_name = models.CharField('Company Short Name', max_length=200, null=True, blank=True)
    company_business_name = models.CharField('Company Business Name', max_length=200, null=True, blank=True)
    company_vat_number = models.CharField('VAT Number', null=True, blank=True, unique=False, max_length=30, help_text="international VAT number (eg. partita IVA)")
    company_tax_code = models.CharField('Tax Code', null=True, blank=True, unique=False, max_length=30, help_text="(eg. codice fiscale)")
    company_address = models.CharField('Company Address', max_length=200, null=True, blank=True)
    company_cap = models.CharField('CAP', max_length=10, null=True, blank=True)
    company_city = models.CharField('City', max_length=200, null=True, blank=True)
    company_province = models.CharField('Province', max_length=200, null=True, blank=True)
    company_country = models.CharField('Country', max_length=200, null=True, blank=True)
    company_mailingaddress = models.TextField('Mailing Address', null=True, blank=True)
    company_phone_number = models.CharField('Phone Number', max_length=100, null=True, blank=True)
    company_fax = models.CharField('FAX', max_length=200, null=True, blank=True)
    company_website = models.CharField('WebSite', max_length=200, null=True, blank=True)
    company_notes = models.TextField('Notes', null=True, blank=True)
    company_is_valid = models.BooleanField('Is Valid', default=True, null=False, blank=False)
    
    company_logo = models.ImageField(upload_to='logos/', default=DEFAULT_LOGO_FILE, help_text="Company logo")
    company_logo_thumbnail = ImageSpecField(source='company_logo',
                                      processors=[ResizeToFit(70, 70)],
                                      format='PNG')

    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)
    # Company Type relation
    company_type = models.ManyToManyField(CompanyType)

    def __str__(self):
        return self.company_name
    
    def display_types(self):
            return join([t.type_name for t in self.company_type.all()])
        
        
    # validation
    def clean(self):
        # check VAT number is unique if defined
        if self.company_vat_number and self.company_vat_number != '':
            if Company.objects.filter(company_vat_number=self.company_vat_number).exclude(pk=self.id).count() > 0:
                raise ValidationError('VAT number %s already in use!' % self.company_vat_number)
                
        # check tax code is unique if defined
        if self.company_tax_code and self.company_tax_code != '':
            if Company.objects.filter(company_tax_code=self.company_tax_code).exclude(pk=self.id).count() > 0:
                raise ValidationError('tax code %s already in use!' % self.company_tax_code)
        return
        
        
    
    def get_logo_or_default(self):
        try:
            if self.company_logo and self.company_logo.file:
                return self.company_logo_thumbnail
            else:
                return None
        except IOError:
            return None





    class Meta:
        ordering = ('company_name',)
        verbose_name_plural = "Companies"

    @property
    def contacts(self):
        relations = []
        for rel in self.ccrelation_set.all():
            relations.append({"role": rel.contact_type.type_name,
                              "contact": {"id": rel.contact.id,
                                          "contact_username": rel.contact.contact_username,
                                          "contact_email": rel.contact.contact_email}})
        return {"relations": relations}


# delete files from filesystem when model is deleted from DB
@receiver(models.signals.post_delete, sender=Company)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.company_logo and instance.company_logo.name != Company.DEFAULT_LOGO_FILE:
        if os.path.isfile(instance.company_logo.path):
            os.remove(instance.company_logo.path)

# delete files from filesystem when model is modified to change the file
@receiver(models.signals.pre_save, sender=Company)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    
    if not instance.pk:
        return False

    try:
        old_file = Company.objects.get(pk=instance.pk).company_logo
    except Company.DoesNotExist:
        return False

    new_file = instance.company_logo
    if not old_file == new_file and old_file.name != Company.DEFAULT_LOGO_FILE:
        if os.path.isfile(old_file.path):
            logger.info("removing old file " + old_file.path)
            os.remove(old_file.path)









@python_2_unicode_compatible
class Contact(models.Model):

    # this is needed to sync with the old CS
    contact_centralservices_id = models.IntegerField('Old Centralservices ID', null=True, blank=True, help_text="ID of this contact in the old CS")

    contact_username = models.CharField('Contact User Name', max_length=200, null=True, blank=True)
    contact_first_name = models.CharField('Contact First Name', max_length=200, null=True, blank=True)
    contact_last_name = models.CharField('Contact Last Name', max_length=200, null=True, blank=True)
    contact_email = models.EmailField('Contact Email', max_length=200, null=False, blank=False, unique=True, default="")
    contact_email_secondary = models.EmailField('Contact Email Secondary', max_length=200, null=True, blank=True)
    contact_phone = models.CharField('Contact Phone', max_length=100, null=True, blank=True)
    contact_phone_secondary = models.CharField('Contact Phone Secondary', max_length=100, null=True, blank=True)
    contact_notes = models.TextField('Notes', null=True, blank=True)

    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)

    # relationship with company
    contact_company = models.ManyToManyField(Company, through='CCRelation')

    def __str__(self):
        return self.contact_username + " - " + self.contact_email

    class Meta:
        ordering = ('contact_email',)
        verbose_name_plural = "Contacts"

    @property
    def role(self):
        relations = []
        for rel in self.ccrelation_set.all():
            relations.append({"role": rel.contact_type.type_name,
                              "company": {"id": rel.company.id, "company_name": rel.company.company_name}})
        return {"relations": relations}


    # validation
    def clean(self):
        # check username is unique if defined
        if self.contact_username and self.contact_username != '':
            if Contact.objects.filter(contact_username=self.contact_username).exclude(pk=self.id).count() > 0:
                raise ValidationError('user name %s already in use!' % self.contact_username)
                
        return


@python_2_unicode_compatible
class CCRelation(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)

    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)

    def __str__(self):
        return self.company.company_short_name + " - " + self.contact.contact_username \
               + " - " + self.contact_type.type_name

    class Meta:
        verbose_name_plural = "CCRelations"


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
        verbose_name_plural = "Services"
