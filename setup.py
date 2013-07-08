from setuptools import setup

setup(
    name='SofiaValleyPlanet',
    version='1.0',
    description='Planet RSS feed for SofiaValley.com',
    author='Alexander Todorov',
    author_email='atodorov@otb.bg',
    url='http://planet.sofiavalley.com',
    install_requires=[
        's3cmd==1.1.0-beta3',
    ],
)
