# What is a sequence object?

A sequence object is a container of items accessed via index. Text strings are technically sequence objects. Remember C strings?

#### Sequence Object Types:

* String
* Lists
* Tuples
* Range Objects

Each of the above support built in functions and slicing.

# Sequence Objects: Strings

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

#### 

#### String Prefixes

* u or U for Unicode​

* r or R for raw string literal \(ignores escape characters\)​

* b or B for byte… is ignored in Python 2 since str is bytes.​

* A ‘u’ or ‘b’ prefix may be followed by a ‘r’ prefix.​

Yes, this stuff is old school and not very Pythonic... but it can't be helped.



## Byte String vs Data String

​

