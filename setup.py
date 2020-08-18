# stdlib
import os

# deps
from setuptools import Command, find_packages, setup


# Dynamically calculate the version based on anon.VERSION
VERSION = __import__("anon").__version__


with open("README.rst") as readme_file:

    def remove_banner(readme):
        # Since PyPI does not support raw directives, we remove them from the README
        #
        # raw directives are only used to make README fancier on GitHub and do not
        # contain relevant information to be displayed in PyPI, as they are not tied
        # to the current version, but to the current development status
        out = []
        lines = iter(readme.splitlines(True))
        for line in lines:
            if line.startswith(".. BANNERSTART"):
                for line in lines:
                    if line.strip() == ".. BANNEREND":
                        break
            else:
                out.append(line)
        return "".join(out)

    README = remove_banner(readme_file.read())


class PublishCommand(Command):
    description = "Publish to PyPI"
    user_options = []

    def run(self):
        # Build & Upload
        # https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
        # https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives
        os.system("python setup.py sdist bdist_wheel")
        os.system("twine upload dist/*")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class CreateTagCommand(Command):
    description = "Create release tag"
    user_options = []

    def run(self):
        os.system("git tag -a %s -m 'v%s'" % (VERSION, VERSION))
        os.system("git push --tags")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


setup(
    name="django-anon",
    version=VERSION,
    packages=find_packages(),
    install_requires=["django-bulk-update", "django-chunkator<2"],
    cmdclass={"publish": PublishCommand, "tag": CreateTagCommand},
    # metadata for upload to PyPI
    description="Anonymize production data so it can be safely used in not-so-safe environments",
    long_description=README,
    long_description_content_type="text/x-rst",
    author="Tesorio",
    author_email="hello@tesorio.com",
    url="https://github.com/Tesorio/django-anon",
    license="MIT",
    platforms=["any"],
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
)
