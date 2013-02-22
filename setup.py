from setuptools import setup, find_packages

version = '1.4.8'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='Products.PloneSurvey',
      version=version,
      description="Plone Survey is a simple product written to collect data from people - feedback on a course, simple data collection etc.",
      long_description=long_description,
      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='Plone, Survey',
      author='Michael Davis',
      author_email='m.r.davis@cranfield.ac.uk',
      url='http://plone.org/products/plone-survey',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'z3c.rml',
      ],
      extras_require={'test': ['plone.app.testing[robot]>=4.2.2']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
