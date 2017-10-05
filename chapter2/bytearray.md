# Bytes\(\)

It's worth re mentioning that Python 2 and Python 3 have differences when it comes to bytes and strings. Python 2 strings are bytes naturally whereas Python 3 is unicode and needs to be defined as bytes. Here are a couple ways to turn Python 3 strings and such.. into bytes. This functionality is backwards compatible with Python 2. It's highly recommended you define Python 2 strings the same way if you are going to be modifying the bytes. Even though it doesn't do anything in Python 2... it will make the job of refactoring code easier, if you had to up Python version to 3.x.

```py
# Method 1 (shortest)
>>> x = b'hello world'
>>> print(x[1])
101 # ASCII dec value

# Method 2 (clean)
>>> x = 'hello world'
>>> y = bytes(x, 'ascii')
>>> print(y)
b'hello world'
>>> print(y[1])
101 # ASCII dec value

# python 2
>>> x = 'hello world'
>>> print ord(x[1]) 
# ord is the inverse of chr()... returns int representing the unicode code point of the argument
101 # Unicode dec value
```

This can go both ways. We can convert these integer representations back into unicode or ASCII strings. 

```py
# Python 2 back to ascii string
>>> x = ord('e')
>>> x
101
>>> y = chr(x)
>>> y
'e'
# convert y into a unicode string (this only works in Python 2 because unicode is default in Python 3)
>>> y = unichr(x)
>>> y
u'e'

# Python 3 back to native unicode string
>>> x = ord('e')
>>> x
101
>>> y = chr(x)
>>> y
'e'
# y is now a unicode string... but how do we turn it into a byte/ascii string?
>>> y = bytes(y, 'ascii')
>>> y
b'e'
# Now y is a python 2 str type... bytes/ascii
```



# Bytearray\(\)

Bytearray\(\) is a mutable sequence of integers in range of 0 &lt;= x &lt; 256; available in Python 2.6 and later​. Byte Arrays are useful when you need to modify individual bytes in a sequence.

