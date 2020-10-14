# deps
from django.test import TestCase

# local
import anon

from .compat import mock


class BaseAnonymizer(anon.BaseAnonymizer):
    class Meta:
        pass

    def __init__(self):
        """
        The reason we set declarations manually in ``__init__`` is because we want to
        patch objects individually for unit testing purposes, without using the
        ``run()`` method. In general cases, declarations will be set by ``run()``
        """
        self._declarations = self.get_declarations()


class BaseTestCase(TestCase):
    def test_get_meta(self):
        class Anon(BaseAnonymizer):
            class Meta:
                pass

        anonymizer = Anon()
        self.assertIsInstance(anonymizer._meta, Anon.Meta)

    def test_get_manager(self):
        manager = object()

        m = mock.Mock()
        m.other_manager = manager

        class Anon(BaseAnonymizer):
            class Meta:
                model = m
                manager = m.other_manager

        anonymizer = Anon()
        self.assertEqual(anonymizer.get_manager(), manager)

    def test_get_queryset(self):
        sample_obj = object()

        m = mock.Mock()
        m.objects.all.return_value = [sample_obj]

        class Anon(BaseAnonymizer):
            class Meta:
                model = m

        anonymizer = Anon()
        result = anonymizer.get_queryset()
        self.assertEqual(result, [sample_obj])
        m.objects.all.assert_called_once()

    def test_patch_object(self):
        fake_first_name = lambda: "foo"  # noqa: E731

        class Anon(BaseAnonymizer):
            first_name = fake_first_name
            last_name = fake_first_name
            raw_data = {1: 2}

        class Obj(object):
            def __init__(self):
                self.first_name = "zzz"
                self.last_name = ""  # empty data should be kept empty
                self.raw_data = {}

        obj = Obj()

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        self.assertEqual(obj.first_name, "foo")
        self.assertEqual(obj.last_name, "")
        self.assertEqual(obj.raw_data, {})

    @mock.patch("anon.base.bulk_update")
    @mock.patch("anon.base.chunkator_page")
    def test_run(self, chunkator_page, bulk_update):
        class Anon(BaseAnonymizer):
            class Meta:
                model = mock.Mock(__name__="x")
                update_batch_size = 42
                manager = object()

            first_name = "xyz"

        class Obj(object):
            def __init__(self):
                self.first_name = "zzz"

        obj = Obj()

        chunkator_page.return_value = [[obj]]

        anonymizer = Anon()
        anonymizer.get_queryset = mock.Mock(return_value=[obj])
        anonymizer.patch_object = mock.Mock()
        anonymizer.run()

        anonymizer.patch_object.assert_called_once_with(obj)
        bulk_update.assert_called_once_with(
            [obj], anonymizer.get_manager(), batch_size=42, update_fields=["first_name"]
        )

    def test_lazy_attribute(self):
        lazy_fn = mock.Mock()
        fake_first_name = anon.lazy_attribute(lazy_fn)

        class Anon(BaseAnonymizer):
            first_name = fake_first_name

        class Obj(object):
            def __init__(self):
                self.first_name = "zzz"

        obj = Obj()

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        lazy_fn.assert_called_once_with(obj)

    def test_lazy_attribute_decorator(self):
        lazy_fn = mock.Mock()

        class Anon(BaseAnonymizer):
            @anon.lazy_attribute
            def first_name(self):
                return lazy_fn(self)

        class Obj(object):
            def __init__(self):
                self.first_name = "zzz"

        obj = Obj()

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        lazy_fn.assert_called_once_with(obj)

    def test_raw_attributes(self):
        class Anon(BaseAnonymizer):
            raw_data = {}

        class Obj(object):
            def __init__(self):
                self.raw_data = {"password": "xyz"}

        obj = Obj()

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        self.assertEqual(obj.raw_data, {})

    def test_clean(self):
        class Anon(BaseAnonymizer):
            line1 = ""
            line2 = ""
            line3 = ""

            def clean(self, obj):
                obj.line1 = "foo"
                obj.line2 = "bar"

        class Obj(object):
            def __init__(self):
                self.line1 = "X"
                self.line2 = "Y"
                self.line3 = "Z"

        obj = Obj()

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        self.assertEqual(obj.line1, "foo")
        self.assertEqual(obj.line2, "bar")
        self.assertEqual(obj.line3, "")

    def test_get_declarations(self):
        # Ensure the order is preserved
        class Anon(BaseAnonymizer):
            a = anon.lazy_attribute(lambda o: 4)
            c = anon.lazy_attribute(lambda o: 6)
            b = anon.lazy_attribute(lambda o: 5)

            def get_queryset(self):
                return []

        anonymizer = Anon()
        self.assertEqual(list(anonymizer.get_declarations().keys()), ["a", "c", "b"])
