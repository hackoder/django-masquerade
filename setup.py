import os
from distutils.core import setup

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

# Use the docstring of the __init__ file to be the description
DESC = " ".join(__import__('masquerade').__doc__.splitlines()).strip()

setup(
    name = "django-masquerade",
    version = __import__('masquerade').get_version().replace(' ', '-'),
    url = 'https://bitbucket.org/technivore/django-masquerade',
    author = 'Matthew Rich',
    author_email = 'matthew@technivore.org',
    description = DESC,
    long_description = read_file('README'),
    packages = ['masquerade','masquerade.templatetags'],
    package_data = {'masquerade': ['templates/masquerade/*.html',]},
    include_package_data = True,
    install_requires=read_file('requirements.txt'),
    classifiers = [
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Django',
    ],
)
