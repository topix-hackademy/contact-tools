from django.test import TestCase

from .models import Service


class ServiceModelTest(TestCase):

    def test_service_representation(self):
        service = Service(service_name='TEST SERVICE')
        service_repr = '%s - %s' % (service.service_name, service.token)
        self.assertEqual(service_repr, str(service))

    def test_verbose_plural_name(self):
        self.assertEqual(str(Service._meta.verbose_name_plural), 'Services')

    def test_creation_token(self):
        service = Service(service_name='TEST SERVICE TOKEN')
        self.assertIsNotNone(service.token)
        self.assertEqual(service.is_valid, True)
        self.assertIsNotNone(service.activation_date)
        self.assertIsNotNone(service.creation_date)
        self.assertIsNone(service.delete_date)

    def test_set_delete_date_on_set_invalid_token(self):
        service = Service(service_name='TEST SERVICE CHANGE')
        service.save()
        service.is_valid = False
        service.save()
        self.assertIsNone(service.delete_date)
        self.assertNotEqual(service.token, 'INVALID')
