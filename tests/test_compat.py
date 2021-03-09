# deps
from django.test import TestCase

# local
from anon.compat import bulk_update

from . import models


class CompatTestCase(TestCase):
    def test_call_bulk_update(self):
        obj = models.person_factory()
        obj.first_name = "xyz"

        bulk_update([obj], {"first_name"}, models.Person.objects)
        obj.refresh_from_db()
        self.assertEqual(obj.first_name, "xyz")
