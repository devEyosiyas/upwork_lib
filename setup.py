import os

import setuptools

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setuptools.setup(
    name='upwork',
    version='1.0.20',
    author='Eyosiyas Bereketab',
    author_email='contact@deveyosiyas.com',
    description='Upwork talent scraper',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    setuprequires=['bs4', 'requests'],
    url='https://github.com/devEyosiyas/upwork_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
