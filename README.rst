.. raw:: html

    <img src="icon.svg" width="128">

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

----

`Icon <icon.svg>`_ made by `Eucalyp <https://www.flaticon.com/authors/eucalyp>`_ from `www.flaticon.com <https://www.flaticon.com/>`_
