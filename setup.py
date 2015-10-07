#!/usr/bin/python
"""Multiple dispatcher on arguments values."""
from setuptools import setup

long_description = """
# dispatk

## Description

This function is inspired by singledispatch of Python 3.4+ (PEP 443),
but the dispatch happens on the key extracted fro the arguments values.

```
from dispatk import dispatk

@dispatk(lambda n: int(n))
def fib(n):
    return fib(n-1) + fib(n-2)
@fib.register(0)
def _(n):
    return 0
@fib.register(1, 2)
def _(n):
    return 1
@fib.register(41)
def _(n):
    return 165580141
```

*register* accepts one or more keys, so

```
@fib.register(1, 2)
def _(n):
    return 1
```

is equivalent to

```
@fib.register(1)
@fib.register(2)
def _(n):
    return 1
```
"""

setup(
    name='dispatk',
    version='0.1',
    author='hephaestus',
    description=__doc__,
    long_description=long_description,
    url='https://github.com/hephs/dispatk',
    keywords='multiple dispatch generic functions genericfunctions decorator',
    platforms=('any',),
    license='MIT',
    py_modules=('dispatk',),
    zip_safe=True,
    install_requires=(),
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
