#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django_shop_area_tax',
    version='0.1',
    author='Tomas Neme',
    author_email='lacrymology@gmail.com',
    url='http://github.com/Lacrymology',
    description = ('Tax cart according to shipping address in django-shop.'),
    packages=find_packages(),
    provides=['django_shop_area_tax', ],
    include_package_data=True,
)
