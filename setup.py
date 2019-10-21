from setuptools import setup, find_packages


VERSION = "0.1"


setup(
    name="django-anon",
    version=VERSION,
    description="Anonymize production data so it can be safely used in not-so-safe environments",
    author="Tesorio",
    url="http://github.com/Tesorio/django-anon",
    license="MIT",
    platforms=["any"],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["django-bulk-update", "django-chunkator"],
)
