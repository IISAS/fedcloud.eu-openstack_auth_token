#!/usr/bin/python

from setuptools import setup

setup(name='openstack_auth_token',
      version='1.0',
      description='Module for logging into Horizon via token',
      author='Viet Tran',
      author_email='tdviet@gmail.com',
      url='https://github.com/tdviet/openstack_auth_token',
      packages=['openstack_auth_token'],
      package_data={'openstack_auth_token': ['templates/*']},
      license='MIT',
      zip_safe=False,
      install_requires=['openstack_auth',]
      )

