# CTypes

CTypes are a foreign function library for Python. It provides C compatible data types and allows calling functions in DLLs or shared libraries. This is useful if we want to utilize a C library for some sort of functionality within Python.

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

If a C library requires arguments to be passed and/or has a return value, it is a good practice to declare them like so:

```py
import ctypes

# Do your system check here if needed

calc = ctypes.CDLL("MyCalc.dll")
addition = calc.addition()
# Declare return type
addition.restype = ctypes.c_int
# Declare argument types
addition.argtypes = [ctypes.c_int, ctypes.c_int]
# Pass arguments
addition(1,2)
```

### Structures

Creating C Structs in Python can be useful. For instance, let's assume a function within a DLL requires a pointer to a struct to be passed. A real world example of this would be a DLL file that communicates with hardware. Below is an example of how to create a C struct using Python ctypes

```py
import ctypes

# Create the struct
class P_Struct(ctypes.Structure):
    _fields_ = [("field_1", ctypes.c_int),
                ("field_2", ctypes.c_char_p)]

# Pass struct values                 
my_struct = P_Struct(1, "Hello World")
# Create a pointer to my_struct
pointer_my_struct = ctypes.pointer(my_struct)

print my_struct.field_1, my_struct.field_2

# Import the DLL and pass pointer_my_struct to the C function requiring a pointer to a struct.
```

**Output:**

```
1 Hello World
```



