from setuptools import setup, find_packages
import codecs
import os


# Get package version
version = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'irods_iscc/version.py')) as file:
    exec(file.read(), version)


# Get description
with codecs.open('README.md', 'r', 'utf-8') as file:
    long_description = file.read()


setup(name='python-irodsclient-iscc',
      version=version['__version__'],
      author='Leonardo Lenoci',
      author_email='l.lenoci@science.leidenuniv.nl',
      description='An ISCC plugin for iRODS python client (PRC)',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='BSD',
      url='https://github.com/ll4strw/python-irodsclient-iscc',
      keywords='irods',
      classifiers=[
                   'License :: OSI Approved :: BSD License',
                   'Development Status :: 3 - Alpha',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10',
                   'Programming Language :: Python :: 3.11',
                   'Programming Language :: Python :: 3.12',
                   'Operating System :: POSIX :: Linux',
                   ],
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
                        # iRODS
                        'python-irodsclient>=2.0.0',
                        # iscc
                        'iscc-core',
                        'iscc-schema',          
                        'python-magic'
                        ]
      )
