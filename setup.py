# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_engineering/__init__.py
from erpnext_engineering import __version__ as version

setup(
	name='erpnext_engineering',
	version=version,
	description='App for adding item revisions and other engineering-related customizations to ERPNext.',
	author='Ability Engineering',
	author_email='red@act.ed',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
