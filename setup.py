from setuptools import setup, find_packages
import os

version = '1.3'

setup(name='sixfeetup.catalogoverrides',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Six Feet Up, Inc.',
      author_email='info@sixfeetup.com',
      url='http://www.sixfeetup.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sixfeetup'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
