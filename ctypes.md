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

**Windows/Linux:**

```
gcc -shared -Wl,-soname,hellworld -o helloworld.so -fPIC helloworld.c
```

**OS X**

```
gcc -shared -Wl,-install_name,helloworld.so -o helloworld.so -fPIC helloworld.c
```

#### testlibwrapper.py

```py
import ctypes

testlib = ctypes.CDLL('helloworld.so')
testlib.myprint()
```



