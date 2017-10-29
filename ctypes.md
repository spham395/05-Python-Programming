# CTypes

CTypes are a foreign function library for Python. It provides C compatible data types and allows calling functions in DLLs or shared libraries. 

**PyDocs:**

[https://docs.python.org/2.7/library/ctypes.html](https://docs.python.org/2.7/library/ctypes.html)

### Data Types

![](/assets/Capture.JPG)

### Importing C Libary

#### helloworld.c

```c
#include <stdio.h>

void myprint(void);
void myprint()
{
    printf("hello world\n");
}
```

```
gcc -shared -Wl, -soname,testlib -o testlib.so -fPIC testlib.c
```

#### testlibwrapper.py

```py
import ctypes

testlib = ctypes.CDLL('helloworld.so')
testlib.myprint()
```



