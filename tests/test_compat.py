# deps
from django.test import TestCase

# local
from anon.compat import bulk_update

from .compat import mock


class CompatTestCase(TestCase):
    @mock.patch("anon.compat.ext_bulk_update")
    def test_call_inbuilt_bulk_update(self, ext_bulk_update):
        class Manager:
            def bulk_update(self, objects, **kwargs):
                pass

        manager = Manager()

        class Obj(object):
            def __init__(self):
                self.first_name = "zzz"

        obj = Obj()

        self.assertTrue(hasattr(manager, "bulk_update"))
        bulk_update(objects=[obj], manager=manager)
        ext_bulk_update.assert_not_called()

    @mock.patch("anon.compat.ext_bulk_update")
    def test_call_ext_bulk_update(self, ext_bulk_update):
        class Manager:
            pass

        manager = Manager()

        class Obj(object):
            def __init__(self):
                self.first_name = "zzz"

        obj = Obj()
        self.assertFalse(hasattr(manager, "bulk_update"))
        bulk_update(
            objects=[obj], manager=manager, batch_size=42, update_fields=["first_name"]
        )
        ext_bulk_update.assert_called_once_with(
            [obj], batch_size=42, update_fields=["first_name"]
        )
