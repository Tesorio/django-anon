# deps
from django.test import TestCase

# local
import anon

from . import models


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
        class Anon(BaseAnonymizer):
            class Meta:
                model = models.Person
                manager = models.PersonAnotherQuerySet

        anonymizer = Anon()
        self.assertEqual(anonymizer.get_manager(), models.PersonAnotherQuerySet)

    def test_get_queryset(self):
        sample_obj = models.person_factory()

        class Anon(BaseAnonymizer):
            class Meta:
                model = models.Person

        anonymizer = Anon()
        result = anonymizer.get_queryset()
        self.assertSequenceEqual(result, [sample_obj])

    def test_patch_object(self):
        fake_first_name = lambda: "foo"  # noqa: E731

        class Anon(BaseAnonymizer):
            first_name = fake_first_name
            last_name = fake_first_name
            raw_data = "{1: 2}"

        obj = models.person_factory(last_name="")  # empty data should be kept empty

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        self.assertEqual(obj.first_name, "foo")
        self.assertEqual(obj.last_name, "")
        self.assertEqual(obj.raw_data, "{1: 2}")

    def test_run(self):
        class Anon(BaseAnonymizer):
            class Meta:
                model = models.Person
                update_batch_size = 42

            first_name = "xyz"

        obj = models.person_factory()

        anonymizer = Anon()
        anonymizer.run()

        obj.refresh_from_db()
        self.assertEqual(obj.first_name, "xyz")

    def test_lazy_attribute(self):
        fake_first_name = anon.lazy_attribute(lambda o: o.last_name)

        class Anon(BaseAnonymizer):
            first_name = fake_first_name

        obj = models.person_factory()

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        self.assertEqual(obj.first_name, obj.last_name)

    def test_lazy_attribute_decorator(self):
        class Anon(BaseAnonymizer):
            @anon.lazy_attribute
            def first_name(self):
                return "xyz"

        obj = models.person_factory()

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        self.assertEqual(obj.first_name, "xyz")

    def test_raw_attributes(self):
        class Anon(BaseAnonymizer):
            raw_data = "{}"

        obj = models.person_factory()

        anonymizer = Anon()
        anonymizer.patch_object(obj)
        self.assertEqual(obj.raw_data, "{}")

    def test_clean(self):
        class Anon(BaseAnonymizer):
            line1 = ""
            line2 = ""
            line3 = ""

            def clean(self, obj):
                obj.line1 = "foo"
                obj.line2 = "bar"

        obj = models.person_factory()

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
