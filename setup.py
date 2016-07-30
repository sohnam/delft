#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def calculate_version():
    initpy = open('delft/_version.py').read().split('\n')
    version = list(filter(lambda x: '__version__' in x, initpy))[0].split('\'')[1]
    return version

package_version = calculate_version()

setup(
    name='DELFT',
    version=package_version,
    author='Randal S. Olson and Rolando Garcia',
    author_email='rso@randalolson.com',
    packages=find_packages(),
    url='https://github.com/rhiever/delft',
    license='GNU/GPLv3',
    #entry_points={'console_scripts': ['tpot=tpot:main', ]},
    description=('A Python tool that automatically optimizes deep learning pipelines using genetic programming. '),
    long_description='''
A Python tool that automatically optimizes deep learning pipelines using genetic programming. 

Contact
=============
If you have any questions or comments about DELFT, please feel free to contact me via:

E-mail: rso@randalolson.com

or Twitter: https://twitter.com/randal_olson

This project is hosted at https://github.com/rhiever/delft
''',
    zip_safe=True,
    install_requires=['numpy', 'scipy', 'pandas', 'scikit-learn', 'deap', 'update_checker', 'tqdm'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    keywords=['deep learning', 'autoencoder', 'pipeline optimization', 'hyperparameter optimization', 'data science', 'machine learning', 'genetic programming', 'evolutionary computation'],
)
