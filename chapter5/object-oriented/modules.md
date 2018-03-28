# Modules

---

Modules are reusable code that can be imported into other scripts or programs. Modules are single files in either .py, .pyc or .pyo format. When a module is imported, code that is not wrapped in a function is executed and the functions themselves are added to the name space... allowing them to be called upon.

### Module Structure

```py
#/usr/lib/python/site-packages/triangle.py

divisor_count_to_find = 500

def triangle_number(n):
    return n*(n+1)/2

def divisors(tn):
    counter = 0
    n_sqrt = int(pow(tn, 0.5))
    for i in range(1, n_sqrt + 1):
        if tn%i == 0:
            counter += 2
    if n_sqrt * n_sqrt == tn:
        counter -= 1
    return counter

def start():
    start_number = 1
    div_numbers = 0
    while (div_numbers < divisor_count_to_find):
        tn = triangle_number(start_number)
        div_numbers = divisors(tn)
        start_number += 1
    print(div_numbers)
    print(tn)

if __name__ == '__main__':
    start()
```

###### Reference: [if \_\_name\_\_ == '\_\_main\_\_':](http://codenhance.com/2015/10/20/wtf-is-if-name-equals-main.html)

In other words, a module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended \(every .py file is a module\). Within a module, the module’s name \(as a string\) is available as the value of the global variable `__name__`.

### Using Modules

```py
import triangle
triangle.start()
triangle.triangle_number(10)
triangle.divisors(10)
triangle.divisor_count_to_find = 100

triangle.start()
# 576 76576500.0 112 73920.0
```

### Importing Modules

```py
# Most common, clean way to do it. Prevents collisions. 
import triangle
triangle.method # Call method

# Same as above except we gave triangle an alias
import triangle as tri
tri.method

# A far more dangerous method... can create collisions.
from triangle import *
```

###### Reference: [Modules](https://docs.python.org/2.7/tutorial/modules.html)

###### 



