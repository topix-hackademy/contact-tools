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


@python_2_unicode_compatible
class Service(models.Model):

    service_name = models.CharField('Service Name', max_length=200)
    token = models.CharField('Token', default=create_uid, max_length=200)
    is_valid = models.BooleanField('Is Valid', default=True)
    creation_date = models.DateTimeField('Creation Date', default=datetime.datetime.now)
    activation_date = models.DateTimeField('Activation Date', default=datetime.datetime.now)
    delete_date = models.DateTimeField('Delete Date', null=True)
    notes = models.TextField('Notes', blank=True)

    def __str__(self):
        return self.service_name + " - " + self.token
