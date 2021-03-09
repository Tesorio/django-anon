# deps
from django.db import models


class PersonAnotherQuerySet(models.QuerySet):
    pass


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)

    raw_data = models.TextField()

    another_manager = models.Manager.from_queryset(PersonAnotherQuerySet)


def person_factory(**kwargs):
    kwargs.setdefault("first_name", "A")
    kwargs.setdefault("last_name", "B")
    kwargs.setdefault("line1", "X")
    kwargs.setdefault("line2", "Y")
    kwargs.setdefault("line3", "Z")
    kwargs.setdefault("raw_data", '{"access_token": "XYZ"}')

    return Person.objects.create(**kwargs)
