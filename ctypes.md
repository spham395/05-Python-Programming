# CTypes

---

**CTypes **provide C compatible data types and allow function calls from DLLs or shared libraries without having to write custom C extensions for every operation. So we can access the functionality of a C library from the safety and comfort of the **Python Standard Library.**

_**CTypes are a Foreign Function Interface \(FFI\) library and provide an API for creating C-compatible datatypes.**_

###### Reference: [CTypes](https://docs.python.org/2.7/library/ctypes.html)



### Loading Libraries:

There are four types of dynamic library loaders available in `ctypes` and two conventions to use them. The classes that represent dynamic and shared libraries are `ctypes.CDLL`, `ctypes.PyDLL`, `ctypes.OleDLL`, and `ctypes.WinDLL`. The last two are only available on Windows.

Differences between `CDLL` and `PyDLL:`

* `ctypes.CDLL`: This class represents loaded shared libraries. The functions in these libraries use the standard calling convention, and are assumed to return `int`. GIL is released during the call.
* `ctypes.PyDLL`: This class works like `CDLL`, but GIL is not released during the call. After execution, the Python error flag is checked and an exception is raised if it is set. It is only useful when directly calling functions from the Python/C API.

To load a library, you can either instantiate one of the preceding classes with proper arguments or call the `LoadLibrary()` function from the submodule associated with a specific class:

* `ctypes.cdll.LoadLibrary()` for `ctypes.CDLL`
* `ctypes.pydll.LoadLibrary()` for `ctypes.PyDLL`
* `ctypes.windll.LoadLibrary()` for `ctypes.WinDLL`
* `ctypes.oledll.LoadLibrary()` for `ctypes.OleDLL`

  The main challenge when loading shared libraries is how to find them in a portable way. Different systems use different suffixes for shared libraries \(`.dll` on Windows, `.dylib` on OS X, `.so` on Linux\) and search for them in different places.

  Both library loading conventions \(the `LoadLibrary()` function and specific library-type classes\) require you to use the full library name. This means all the predefined library prefixes and suffixes need to be included. For example, to load the C standard library on Linux, you need to write the following:

```
>>> import ctypes
>>> ctypes.cdll.LoadLibrary('libc.so.6')
<CDLL 'libc.so.6', handle 7f0603e5f000 at 7f0603d4cbd0>
```

Fortunately, the `ctypes.util` submodule provides a `find_library()` function that allows to load a library using its name without any prefixes or suffixes and will work on any system that has a predefined scheme for naming shared libraries:

```
>>> import ctypes
>>> from ctypes.util import find_library
>>> ctypes.cdll.LoadLibrary(find_library('c'))
<CDLL '/usr/lib/libc.dylib', handle 7fff69b97c98 at 0x101b73ac8>
>>> ctypes.cdll.LoadLibrary(find_library('bz2'))
<CDLL '/usr/lib/libbz2.dylib', handle 10042d170 at 0x101b6ee80>
>>> ctypes.cdll.LoadLibrary(find_library('AGL'))
<CDLL '/System/Library/Frameworks/AGL.framework/AGL', handle 101811610 at 0x101b73a58>

#Linux
```

### Calling C functions using ctypes

When the library is successfully loaded, the common pattern is to store it as a module-level variable with the same name as library. The functions can be accessed as object attributes, so calling them is like calling a Python function from any other imported module:

```
>>> import ctypes
>>> from ctypes.util import find_library
>>> 
>>> libc = ctypes.cdll.LoadLibrary(find_library('c'))
>>> 
>>> libc.printf(b"Hello world!\n")
Hello world!
13
```

Unfortunately, all the built-in Python types except integers, strings, and bytes are incompatible with C datatypes and thus must be wrapped in the corresponding classes provided by the `ctypes` module.

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



