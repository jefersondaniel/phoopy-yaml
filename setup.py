from setuptools import setup
import phoopy.yaml

long_description = open('README.rst', 'r').read()

setup(
    name='phoopy-yaml',
    version=phoopy.yaml.__version__,
    packages=['phoopy', 'phoopy.yaml'],
    setup_requires=['wheel'],
    install_requires=['PyYAML>=3.13'],
    description="Yaml parsing library for phoopy framework",
    long_description=long_description,
    url='https://github.com/phoopy/phoopy-yaml',
    author='Phoopy',
    author_email='reisraff@gmail.com',
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
