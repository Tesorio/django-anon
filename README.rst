.. BANNERSTART
.. Since PyPI does not support raw directives, we remove them from the README
..
.. raw directives are only used to make README fancier on GitHub and do not
.. contain relevant information to be displayed in PyPI, as they are not tied
.. to the current version, but to the current development status
.. raw:: html

    <p align="center">
      <a href="https://github.com/Tesorio/django-anon">
        <img src="https://raw.githubusercontent.com/Tesorio/django-anon/master/icon.svg?sanitize=true" width="128">
      </a>
    </p>

    <h1 align="center">django-anon</h1>
    <p align="center">
      <strong>
        <img src="https://github.githubassets.com/images/icons/emoji/shipit.png" width="16"> Anonymize production data so it can be safely used in not-so-safe environments
      </strong>
    </p>

    <p align="center">
      <a href="https://github.com/Tesorio/django-anon/actions?query=branch%3Amaster">
        <img src="https://github.com/Tesorio/django-anon/workflows/CI/badge.svg?branch=master">
      </a>
      <a href="https://django-anon.readthedocs.io/en/latest/">
        <img src="https://readthedocs.org/projects/pip/badge/?version=latest&style=flat">
      </a>
      <a href="https://github.com/Tesorio/django-anon/blob/master/LICENSE.txt">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg">
      </a>
      <a href="https://pypi.org/project/django-anon/">
        <img src="https://img.shields.io/pypi/v/django-anon.svg?color=blue">
      </a>
    </p>
    
    <p align="center">
      <a href="#installation">
        Install
      </a>
      |
      <a href="https://django-anon.readthedocs.io/en/latest/introduction.html#table-of-contents">
        Read Documentation
      </a>
      |
      <a href="https://pypi.org/project/django-anon/">
        PyPI
      </a>
      |
      <a href="https://github.com/Tesorio/django-anon/blob/master/CONTRIBUTING.rst">
        Contribute
      </a>
    </p>
.. BANNEREND

**django-anon** will help you anonymize your production database so it can be
shared among developers, helping to reproduce bugs and make performance improvements
in a production-like environment.

.. image:: https://raw.githubusercontent.com/Tesorio/django-anon/master/django-anon-recording.gif

.. start-features

Features
========

.. start-features-table

.. csv-table::

   "🚀", "**Really fast** data anonymization and database operations using bulk updates to operate over huge tables"
   "🍰", "**Flexible** to use your own anonymization functions or external libraries like `Faker <https://faker.readthedocs.io/en/latest/index.html>`_"
   "🐩", "**Elegant** solution following consolidated patterns from projects like `Django <https://djangoproject.com/>`_ and `Factory Boy <https://factoryboy.readthedocs.io/en/latest/index.html>`_"
   "🔨", "**Powerful**. It can be used on any projects, not only Django, not only Python. Really!"

.. end-features-table
.. end-features
.. start-table-of-contents

Table of Contents
=================
.. contents::
   :local:

.. end-table-of-contents
.. start-introduction


Installation
------------

.. code::

   pip install django-anon

   
Supported versions
------------------

* Python (2.7, 3.7)
* Django (1.8, 1.11, 2.2, 3.0)


License
-------

`MIT <https://github.com/Tesorio/django-anon/blob/master/LICENSE>`_

.. end-introduction
.. start-usage


Usage
-----

Use ``anon.BaseAnonymizer`` to define your anonymizer classes:

.. code-block:: python

   import anon

   from your_app.models import Person

   class PersonAnonymizer(anon.BaseAnonymizer):
      email = anon.fake_email
      
      # You can use static values instead of callables
      is_admin = False

      class Meta:
         model = Person

   # run anonymizer: be cautious, this will affect your current database!
   PersonAnonymizer().run()


Built-in functions
~~~~~~~~~~~~~~~~~~

.. code:: python

   import anon

   anon.fake_word(min_size=_min_word_size, max_size=20)
   anon.fake_text(max_size=255, max_diff_allowed=5, separator=' ')
   anon.fake_small_text(max_size=50)
   anon.fake_name(max_size=15)
   anon.fake_username(max_size=10, separator='')
   anon.fake_email(max_size=25, suffix='@example.com')
   anon.fake_url(max_size=50, scheme='http://', suffix='.com')
   anon.fake_phone_number(format='999-999-9999')


Lazy attributes
~~~~~~~~~~~~~~~

Lazy attributes can be defined as inline lambdas or methods, as shown below,
using the ``anon.lazy_attribute`` function/decorator.

.. code-block:: python

   import anon

   from your_app.models import Person

   class PersonAnonymizer(anon.BaseAnonymizer):
      name = anon.lazy_attribute(lambda o: 'x' * len(o.name))

      @lazy_attribute
      def date_of_birth(self):
         # keep year and month
         return self.date_of_birth.replace(day=1)

      class Meta:
         model = Person


The clean method
~~~~~~~~~~~~~~~~

.. code-block:: python

   import anon

   class UserAnonymizer(anon.BaseAnonymizer):
      class Meta:
         model = User

      def clean(self, obj):
         obj.set_password('test')
         obj.save()


Defining a custom QuerySet
~~~~~~~~~~~~~~~~~~~~~~~~~~

A custom QuerySet can be used to select the rows that should be anonymized:

.. code-block:: python

   import anon

   from your_app.models import Person

   class PersonAnonymizer(anon.BaseAnonymizer):
      email = anon.fake_email

      class Meta:
         model = Person

      def get_queryset(self):
         # keep admins unmodified
         return Person.objects.exclude(is_admin=True)


High-quality fake data
~~~~~~~~~~~~~~~~~~~~~~

In order to be really fast, **django-anon** uses it's own algorithm to generate fake data. It is
really fast, but the generated data is not pretty. If you need something prettier in terms of data,
we suggest using `Faker <https://faker.readthedocs.io/en/latest/index.html>`_, which can be used
out-of-the-box as the below:

.. code-block:: python

   import anon

   from faker import Faker
   from your_app.models import Address

   faker = Faker()

   class PersonAnonymizer(anon.BaseAnonymizer):
      postalcode = faker.postalcode

      class Meta:
         model = Address

.. end-usage

Changelog
---------

Check out `CHANGELOG.rst <https://github.com/Tesorio/django-anon/blob/master/CHANGELOG.rst>`_ for release notes

Contributing
------------

Check out `CONTRIBUTING.rst <https://github.com/Tesorio/django-anon/blob/master/CONTRIBUTING.rst>`_ for information about getting involved

----

`Icon <icon.svg>`_ made by `Eucalyp <https://www.flaticon.com/authors/eucalyp>`_ from `www.flaticon.com <https://www.flaticon.com/>`_
