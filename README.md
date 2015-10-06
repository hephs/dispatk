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

## Links

+ [multiple dispatch](https://en.wikipedia.org/wiki/Multiple_dispatch)
+ [multipledispatch pypi](https://pypi.python.org/pypi/multipledispatch/)
+ [PEP 443](https://www.python.org/dev/peps/pep-0443/)
+ [singledispatch docs](https://docs.python.org/3/library/functools.html#functools.singledispatch)
+ [singledispatch pypi](https://pypi.python.org/pypi/singledispatch)

