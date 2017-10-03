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

**Python 2**

```py
>>> x = "I am a string"
>>> type(x)
<type 'str'>​
>>> x​
'I am a string'
>>> hex(ord(x[0]))​
0x49​
```

**Python 3**

```py
>>> x = 'I am a string'.encode('ASCII')​
>>> type(x)​
<class 'bytes'>​
>>> print(hex(x[0]))​
0x49 # ASCII code for capital I​
```

```py
>>> x = b'I am a string' # Doing this in Python 2 makes no difference
>>> type(x)
<class 'bytes'>
```

### Unicode Strings

**Python 2**

```py
>>> x = u"I am a unicode string”"
>>> type(x)​
<type 'unicode'>​
>>> y = unicode("Look at me! I’m a unicode string.")​
>>> type(y)​
<type 'unicode'>​
# You can use ‘…’ quotes “…” quotes or “””…””” quotes​
```

**Python 3**

```py
>>> x = 'I am a unicode string”'
>>> type(x)​
<class 'str'>​
​
# class str is unicode in Python 3 natively​
# You can use ‘…’ quotes “…” quotes or “””…””” quotes​
```





### Slicing

Slicing allows you to grab a substring of a string

**Grabbing a specific element**

```py
>>> x = "hello world"​
>>> print x[4] # grabs 5th element​
o
```

**Grab a range of elements**

```py
>>> x = "hello world”"
>>> print x[4:9] # grabs 5th element to between 9th element​
o wor
```

**Grabbing backwards from the last element**

```py
>>> x = "hello world”"
>>> print x[-3] # grabs 8th element (3 elements from end)​
r
```

### 

### User Input

There are a few ways to capture user input in Python. The most common are **raw\_input\(\)** in Python 2 and **input\(\)** in Python 3. It is important that you use raw\_input\(\) in Python 2... as input\(\) has security vulnerabilities. In Python 3, input\(\) takes user input as a string, no matter the input. On the other hand, input\(\) in Python 2 will take user input as the type presented. This can lead to users implementing false bools and such.

**Python 2**

```py
>>> name = raw_input("What is your name? ")
What is your name? <user input>
>>> name
<user input>
```

**Python 3**

```py
>>> name = input("What is your name? ")
What is your name? <user input>
>>> name
<user input>
```

As you more than likely guessed, the user input is assigned to the variable _name_ and stored as a string. From here, you can treat var name as any other regular string.

### Useful String Methods

* **string.upper\(\) **\# Outputs string as uppercase​

* **string.lower\(\) **\# Outputs string as lowercase​

* **len\(string\)** \# Outputs string length​

* **symbol.join\(string/list\)** \# Most commonly used to join list items, outputs string.​

* **string.split\(symbol \)**\# Most commonly used to split a string up into a list of items, outputs list.​



