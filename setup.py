import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='url-obfuscate',
    version='0.1',
    packages=find_packages(),

    # Dependencies
    install_requires=['Django>=1.6', 'pycrypto==2.6.1'],

    # Metadata for PyPI
    author='Laura Manzur',
    author_email='lmanzurv@gmail.com',
    maintainer='Laura Manzur',
    maintainer_email='lmanzurv@gmai.com',
    description='This is a Django application that provides methods to obfuscate/deobfuscate URLs',
    long_description=README,
    license='Apache License',
    url='https://github.com/lmanzurv/url_ofbuscate',
    keywords='django url obfuscate obfuscation',
    download_url='https://github.com/lmanzurv/url_ofbuscate',
    bugtrack_url='https://github.com/lmanzurv/url_ofbuscate/issues',
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: Academic Free License (AFL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
    ]
)
