# What is a sequence object?

A sequence object is a container of items accessed via index. Text strings are technically sequence objects. Remember C strings?

#### Sequence Object Types:

* String
* Lists
* Tuples
* Range Objects

Each of the above support built in functions and slicing.

## Sequence Objects: Strings

**Strings are immutable! **They need to be reassigned. There are two independent types of strings:

* ASCII: Default strings for Python 2
* Unicode \(UTF-8\): Default strings for Python 3

To declare a string, use one of the following. There is no Pythonic way aside from keeping it as simple and clean as possible.

* 'single quotes'
* "double quotes"
* "\"escaped\" quotes"
* """triple quoted-multiline"""
* r"\"raw\" strings"

![](/assets/Screen Shot 2017-10-02 at 10.47.01 AM.png)

### String Prefixes

* u or U for Unicode​

* r or R for raw string literal \(ignores escape characters\)​

* b or B for byte… is ignored in Python 2 since str is bytes.​

* A ‘u’ or ‘b’ prefix may be followed by a ‘r’ prefix.​

Yes, this stuff is old school and not very Pythonic... but it can't be helped.

### Byte String vs Data String

Byte Strings are simply just a sequence of bytes. In Python 2, str is an alias of ASCII bytes. In other words, they are used interchangeably. In Python 3 on the other hand, str is it's own type... utilizing Unicode \(utf-8\). Whereas the bytes type in Python 3 is still a bytes object in ASCII; an array of integers.

​

**Python 2**![](/assets/Screen Shot 2017-10-03 at 10.09.01 AM.png)

**Python 3**![](/assets/Screen Shot 2017-10-03 at 10.10.15 AM.png)

