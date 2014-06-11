import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = ['rauth']

setup(name='Untappd Client Library',
    version='0.1',
    description='Library for accessing the Untappd API in Python',
    long_description=README,
    author='Tony Blank',
    author_email='hiredgun79@gmail.com',
    url='https://untappd.como',
    keywords=['untappd', 'beer', 'api', 'thirsty'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
