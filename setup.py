try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


config = {
    'description': 'Python API Client for Google Sheets API',
    'author': 'Henry Marment',
    'url': '',
    'download_url': '',
    'author_email': 'henry@adsquare.com',
    'version': '0.1',
    'install_requires': requirements,
    'packages' : find_packages(),
    'scripts': [],
    'name': 'pygsheets'
}

setup(**config)