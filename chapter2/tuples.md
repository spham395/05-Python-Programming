# Tuples

---

Tuples are very similar to lists. The major difference is that tuples are **IMMUTABLE! **So just like strings and numbers, you cannot modify it's contents without reassigning. This also means that the length of tuples are set in stone. Parentheses \(round brackets like these\) are commonly used to declare tuples. But unlike lists, the parentheses are not required! You can declare tuples by just using commas.

```py
# common method to declare tuples
>>> someTuple = (1,2,3,4,5)
# alternative method
>>> neatTuple = 1,2,3,4,5

>>> print neatTuple
(1, 2, 3, 4, 5)

# What does the below do?
>>> del someTuple[2]
```

### Why Use Tuples?

Tuples are still sequence objects. You can still:​

* Implement all common sequence operations​

* Slice​

* Index​

**Useful for:**​

* Returning multiple results from functions​

* Since they are immutable, they can be used as keys for a dictionary.​

# xrange\(\)

xrange\(\) is Similar to range\(\), returns xrange object \(sequence object\) instead of list. Intended to be a simple, efficient \(uses less resources due to one-at-time loading method vs loading all increments\) and a fast way to iterate through a range. In most cases, xrange\(\) will be the way to go. The only time you should use range\(\) is when you are going to be iterating over the list multiple times. This is because xrange\(\) will use more processing power over the length of the repeated iteration vs range... which will return a list and that list will stay and can be referenced whenever.

```py
>>> for i in xrange(10):
>>>    print i
0
1
2
3
4
5
6
7
8
9

# Only even numbers
>>> for i in xrange(2, 10, 2):
>>>     print i
2
3
6
8

# Negative numbers
>>> for i in xrange(-1, -10, -1):
>>>     print i
-1
-2
-3
-4
-5
-6
-7
-8
-9
```

# Buffer \(memoryview\)

Buffer \(memoryview\) is useful if you don’t want to or can’t hold multiple copies of data in memory. It can also be lightening fast since it's not copying the data. Buffer \(or memoryview\) essentially expose \(by reference\) raw byte arrays to other Python objects. That means the argument passed must be in bytes \(ints representing bytes\).

```py
# Python 2
>>> x = b'100'
>>> buffer(x)
<read-only buffer for 0x10b1acc60, size -1, offset 0 at 0x10b1a9930>

# Python 3
>>> x = b'100'
>>> memoryview(x)
<memory at 0x1040b1948>
```

### Practical Example

Below is a great example displaying how much resources and time buffer\(memoryview\) can save you. Copy, paste and run the code yourself. The first set of prints will be normal... the second will be using memoryview. Notice the amount of time it takes to complete each set of operation in bytes vs memoryview. While that may seem small... when more data is being manipulated, the time increases exponentially. A quick example can be found by running the same code below, but moving the prints into the while loops.

```py
import time
for n in (100000, 200000, 300000, 400000):
    data = 'x'*n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print 'bytes', n, time.time()-start

for n in (100000, 200000, 300000, 400000):
    data = 'x'*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print 'memoryview', n, time.time()-start
```



