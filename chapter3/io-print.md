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

# Padding numbers
print '%4d' % (50,)
  50

# Padding Floating Points
print '%06.2f' % (3.141592653589793,)
003.14

# Name Placeholders
things = {'car': 'BMW E30', 'motorcycle': 'Harley FXDX'}
print 'My fav car %(car)s and motorcycle %(motorcycle)s' % things
'My fav car BMW E30 and motorcycle Harley FXDX'
```

### .format\(\)

Format\(\) is the latest formatting functionality. PEP8 high encourages the use of .format\(\) whenever possible. .format\(\) includes most of the previous functionality with a ton of added functionality as well. Below is just SOME of the built in .format\(\) functionality. Keep in mind, you can create custom functionality with .format\(\). Take a look at the docs and below and experiment!

```py
​# Basic Positional Formatting
print '{} {}!'.format('Hello', 'World')
'Hello World!'

# Basic Positional Formatting
print "{!s} {!s}".format("Hello", "World")
'Hello World!'

# Actual Positional Formatting
# EXCLUSIVE
print '{1} {0}!'.format('World', 'Hello')
'Hello World!'

# Padding 10 left
print '{:>10}'.format('test')
'      test'

# Negative Padding 10 right
print '{:<10}'.format('test')
'test      '

# Changing Padding Character
# EXCLUSIVE
print '{:_>10}'.format('test')
'______test'

# Center Align
# EXCLUSIVE
print '{:_^10}'.format('test')
'___test___'

# Truncating Long Strings
print '{:.5}'.format('what in the world')
'what '

# Truncating and padding
'{:10.5}'.format('what in the world')
'     what'

# Numbers
print '{:d}'.format(50)
50

# Floats
print '{:f}'.format(3.123513423532432)
3.123513

# Padding numbers
print '{:4d}'.format(50)
  50

# Padding Floating Points
print '{:06.2f}'.format(3.141592653589793)
003.14

# Name Placeholders
things = {'car': 'BMW E30', 'motorcycle': 'Harley FXDX'}
print 'My fav car {car} and motorcycle {motorcycle}'.format(**things)
'My fav car BMW E30 and motorcycle Harley FXDX'

# Keyword Arguments
# EXCLUSIVE
print '{first} {last}'.format(first='Old', last='Gregg')
'Old Gregg'


# Date and Time
# EXCLUSIVE
from datetime import datetime
print '{:%Y-%m-%d %H:%M}'.format(datetime(2017, 10, 17, 10, 45))
2017-10-17 10:45
```

# Lab 3C: Formatting

Create your own mad libs game asking the user for input to fill in the blanks. Print out using .format\(\).

\(Humor encouraged\)

