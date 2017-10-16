# I/O Print

Python print/print\(\) is very powerful... taking styling from C string formating and adding some of it's own functionality; allowing for deep functionality. Pull up PyDocs and reference Py2 and Py3 print, %, and formatting.

**Python 2 Basic:**

```py
print "hello"
print 1+1
print 'Hello' + 'world'
print 'Hello' , 'World')
```

**Python 3 Basic:**

```py
print("hello")
print(1+1)
print('Hello' + 'World')
print('Hello' , 'World')
```

### % Formatting

% formatting follows C style and is being phased out. It is highly recommend to use .format\(\)… but have practice with both!

```py
​# Basic Positional Formatting
print "%s World!" % "Hello"
'Hello World!'

# Basic Positional Formatting
print "%s %s!" % ("Hello", "World")
'Hello World!'

# Padding 10 left
print '%10s' % ('test',)
'      test'

# Negative Padding 10 right
print '%-10s' % ('test',)
'test          '

# Truncating Long Strings
print '%.5s' % ('what in the world',)
'what '

# Truncating and padding
print '%10.5s' % ('what in the world',)
'     what'

# Numbers
print '%d' % (50,)
50

# Floats
print '%f' % (3.123513423532432)
3.123513
```



