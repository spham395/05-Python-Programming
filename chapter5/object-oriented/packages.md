# Packages

Packages are a way to structure Python's module namespace. Essentially a package is just a collection of modules. A module named \_**\_**_**init.py\_\_ **_is required to treat the directory as a package. This file can contain initialization code... but it's often best to leave it blank. 

### Package Structure

```py
math_stuff/ #top directory 
    __init__.py #special module 
    fib.py #fib module 
    triangle.py #triangle module 
    Calculator.py #calculator class module
more_math_stuff/ #additional package 
    __init__.py 
        other_modules.py
```

#### How to Import From a Package

So let's take the package below and walk through an import.

```py
math_stuff/
    __init__.py
    fib.py
    triangle.py # run this file
    Calculator.py
    more_math_stuff/
        __init__.py 
        other_modules.py # import this module
```

```py
from more_math_stuff import other_modules as om

om.do_something()
```



