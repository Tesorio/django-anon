.. raw:: html

    <img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE4LjEuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgMTQuNzg1IDE0Ljc4NSIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTQuNzg1IDE0Ljc4NTsiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPGc+DQoJCTxwb2x5Z29uIHN0eWxlPSJmaWxsOiMwMzAxMDQ7IiBwb2ludHM9IjExLjA0Nyw0LjU0NCAxMS4wNDcsNS4zMDMgMTQuMDI3LDUuMzAzIDE0LjAyNyw5LjQ4MiAxMS4wNDcsOS40ODIgMTEuMDQ3LDEwLjI0IA0KCQkJMTQuNzg1LDEwLjI0IDE0Ljc4NSw0LjU0NCAJCSIvPg0KCQk8cG9seWdvbiBzdHlsZT0iZmlsbDojMDMwMTA0OyIgcG9pbnRzPSI4LjEzMSw5LjQ4MiAwLjc1OCw5LjQ4MiAwLjc1OCw1LjMwMyA4LjEzMSw1LjMwMyA4LjEzMSw0LjU0NCAwLDQuNTQ0IDAsMTAuMjQgDQoJCQk4LjEzMSwxMC4yNCAJCSIvPg0KCQk8cGF0aCBzdHlsZT0iZmlsbDojMDMwMTA0OyIgZD0iTTEwLjEzOCwxMS44MjZjLTAuMDMxLTAuMDMyLTAuMDUzLTAuMDY4LTAuMDcxLTAuMTE1VjMuMjI3bC0wLjAwMi0wLjA1OA0KCQkJYzAuMDE1LTAuMDc0LDAuMDQ1LTAuMTM1LDAuMDk0LTAuMTg2QzEwLjMwNCwyLjgzMiwxMC41ODYsMi44LDEwLjc5NywyLjhoMC4zOTVWMS44MTNoLTAuMzk1Yy0wLjUwNiwwLTAuOTE0LDAuMTIyLTEuMjE1LDAuMzYyDQoJCQlDOS4yNzksMS45MTgsOC44NjEsMS43ODgsOC4zMzksMS43ODhINy45NDR2MC45ODhoMC4zOTVjMC4yMSwwLDAuNDkyLDAuMDMxLDAuNjM3LDAuMTgzQzkuMDA4LDIuOTkxLDkuMDMyLDMuMDMsOS4wNDgsMy4wNzUNCgkJCXY4LjUwM2MwLDAuMDA1LTAuMDAxLDAuMTQzLTAuMTAzLDAuMjQ4Yy0wLjE0NiwwLjE1Mi0wLjQyOCwwLjE4NS0wLjYzOSwwLjE4NUg3LjkxMXYwLjk4NmgwLjM5NWMwLjUxOCwwLDAuOTMzLTAuMTI4LDEuMjM1LTAuMzc5DQoJCQljMC4zMDMsMC4yNTMsMC43MTcsMC4zNzksMS4yMzQsMC4zNzloMC4zOTZ2LTAuOTg2aC0wLjM5NkMxMC41NjQsMTIuMDEsMTAuMjgzLDExLjk3OCwxMC4xMzgsMTEuODI2eiIvPg0KCTwvZz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjwvc3ZnPg0K" width="128">

django-anon
-----------

This app emerged from the need to create a database copy that is close to a
production database in terms of size and relationships, but that should also
not contain any sensitive/identifiable data.

While some other apps like `Factory Boy <https://factoryboy.readthedocs.io/en/latest/index.html>`_
makes it easy to create fixtures that can be used to create a fake database, it
may be a hard task to create one that is really close to what you have in
production, specially when you think about all kinds of relationships between
objects that may exist in a real world usage.

We defined some rules that we should follow to make this work as we need:

* It must be **safe™** – the app does not provide an easy way to mess with your
  stuff.
* It must be **fast™** – while you can use `Faker <https://faker.readthedocs.io/en/latest/index.html>`_,
  that generates high-quality fake data, it is up to you. We provide a built-in
  library that generates fake data with focus on being fast, as your database
  may be huge.
* It must be **fun™** – we love Factory Boy, so we built a similar experience
  for writing your anonymizers. It's fun and really flexible!

Talk is cheap. Show me the code!

.. code-block:: python

   import django_anon as anon

   class UserAnonymizer(anon.BaseAnonymizer):
      email = anon.fake_email

      class Meta:
         model = User

      def clean(self, obj):
         obj.set_password('test')
         obj.save()


Basic Usage
-----------

Use :class:`anon.BaseAnonymizer` to define your anonymizer classes:

.. code-block:: python

   import django_anon as anon
   from your_app.models import Person

   class PersonAnonymizer(anon.BaseAnonymizer):
      email = anon.fake_email

      class Meta:
         model = Person

   # run anonymizer: be cautious, this will affect your current database!
   PersonAnonymizer().run()


Static data
-----------

.. code-block:: python

   import django_anon as anon
   from your_app.models import Person

   class PersonAnonymizer(anon.BaseAnonymizer):
      is_admin = False
      some_other_field = ''

      class Meta:
         model = Person


Lazy data
---------

Lazy attributes can be defined as inline lambdas or methods, as shown below,
using the :func:`anon.lazy_attribute` function/decorator.

.. code-block:: python

   import django_anon as anon
   from your_app.models import Person

   class PersonAnonymizer(anon.BaseAnonymizer):
      name = anon.lazy_attribute(lambda o: 'x' * len(o.name))

      @lazy_attribute
      def date_of_birth(self):
         # keep year and month
         return self.date_of_birth.replace(day=1)

      class Meta:
         model = Person


Clean method
------------

.. code-block:: python

   import django_anon as anon

   class UserAnonymizer(anon.BaseAnonymizer):
      class Meta:
         model = User

      def clean(self, obj):
         obj.set_password('test')
         obj.save()


Custom QuerySet
---------------

A custom QuerySet can be used to select the rows that should be anonymized:

.. code-block:: python

   import django_anon as anon
   from your_app.models import Person

   class PersonAnonymizer(anon.BaseAnonymizer):
      email = anon.fake_email

      class Meta:
         model = Person

      def get_queryset(self):
         # keep admins unmodified
         return Person.objects.exclude(is_admin=True)


Faker
-----

`Faker <https://faker.readthedocs.io/en/latest/index.html>`_ can be used to
provide high-quality fake data:

.. code-block:: python

   import django_anon as anon
   from faker import Faker
   from your_app.models import Address

   faker = Faker()

   class PersonAnonymizer(anon.BaseAnonymizer):
      postalcode = faker.postalcode

      class Meta:
         model = Address
