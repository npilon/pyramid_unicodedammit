from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='pyramid_unicodedammit',
      version=version,
      description="Make a best effort to deal with bizarre query strings",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Nicholas Pilon',
      author_email='npilon@gmail.com',
      url='https://github.com/npilon/pyramid_unicodedammit',
      license='Apache 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'pyramid>=1.2dev',
          'beautifulsoup4>=4.5.0',
          ],
      )
