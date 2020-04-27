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



0.1
~~~

* Initial release


master
~~~~~~

* Added test for Django 3 using Python 3.7 in tox.ini
* Improved performance of fake_text
* Improved performance of BaseAnonymizer.patch_object
* Fix bug with get_queryset not being treated as reserved name
* Improved performance of fake_username
* Removed rand_range argument from fake_username (backwards incompatible)
* Changed select_chunk_size and update_batch_size to saner defaults
