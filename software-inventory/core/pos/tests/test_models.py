from django.test import TestCase
from ..models import Client


class ModelsTestCase(TestCase):

    def test_get_full_name(self):
        full_name = Client.objects.create(
            names="Yamil",
            dni="72131087",
            birthdate="2000-01-25",
            address="Arequipa",
            gender="male"
        )
        full_name.save()

        self.assertEqual(full_name.get_full_name(), 'Yamil (72131087)')