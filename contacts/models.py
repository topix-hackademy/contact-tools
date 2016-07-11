from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class CompanyType(models.Model):

    type_name = models.CharField('Company Type', max_length=200)
    is_valid = models.BooleanField('Is Valid', default=True)
    creation_date = models.DateTimeField('Date Created', auto_now_add=True)

    def __str__(self):
        return self.type_name