Changelog
=========

**django-anon**'s release numbering works as follows:

* Versions are numbered in the form **A.B** or **A.B.C.**
* **A.B** is the feature release version number. Each version will be mostly backwards compatible with the previous release. Exceptions to this rule will be listed in the release notes.
* **C** is the patch release version number, which is incremented for bugfix and security releases. These releases will be 100% backwards-compatible with the previous patch release.


Releases
--------

.. contents::
   :local:


master
~~~~~~

...


0.3.2
~~~~~

* Fixed an infinite loop condition in ``fake_username`` when using the default empty separator


0.3.1
~~~~~

* Fixed bug that happens with newer versions of Django (> 2.2) #63


0.3
~~~

* Updated bulk_update method to use Django's built-in method if available
* Changed default ``max_size`` for ``fake_email`` to ``40``
* Fixed error in ``fake_text`` when ``max_size`` is too short


0.2
~~~

* Added test for Django 3 using Python 3.7 in tox.ini
* Improved performance of fake_text
* Improved performance of BaseAnonymizer.patch_object
* Fix bug with get_queryset not being treated as reserved name
* Improved performance of fake_username
* Removed rand_range argument from fake_username (backwards incompatible)
* Changed select_chunk_size and update_batch_size to saner defaults


0.1
~~~

* Initial release
