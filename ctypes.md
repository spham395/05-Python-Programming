# CTypes

CTypes are a foreign function library for Python. It provides C compatible data types and allows calling functions in DLLs or shared libraries. This is useful if we want utilize a C library for some sort of functionality within Python.

**PyDocs:**

[https://docs.python.org/2.7/library/ctypes.html](https://docs.python.org/2.7/library/ctypes.html)

### Data Types

![](/assets/Capture.JPG)

### Importing a C Libary

Bellow is an example of how to import a very small C library that simply prints "hello world".

#### helloworld.c

```c
#include <stdio.h>

void myprint(void);
void myprint()
{
    printf("hello world\n");
}
```

**Windows/Linux:**

```
gcc -shared -Wl,-soname,hellworld -o helloworld.so -fPIC helloworld.c
```

**OS X:**

```
gcc -shared -Wl,-install_name,helloworld.so -o helloworld.so -fPIC helloworld.c
```

#### testlibwrapper.py

```py
import ctypes
import platform

# Import the library
# If you did not create a dll, only use the else section of the code
if platform.system() == 'Windows':
    testlib = ctypes.CDLL('helloworld.dll')
else:
    testlib = ctypes.CDLL('helloworld.so')

# Call upon the function in C
testlib.myprint()
```

Then execute the testlibwrapper.py using either Python 2.7 or Python 3.x

**Output:**

```
hello world
```

### Defining Argument Types and Return Types

If a C library requires arguments to be passed, it is a good practice to pass them like so:

```py
import ctypes

# Do your system check here if needed

calc = ctypes.CDLL("MyCalc.dll")
addition = calc.addition()
addition.restype = ctypes.c_int
addition.argtypes = [ctypes.c_int, ctypes.c_int]
addition(1,2)
```



