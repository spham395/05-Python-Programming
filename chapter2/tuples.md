# Tuples

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

xrange\(\) is Similar to range\(\), returns xrange object \(sequence object\) instead of list. Intended to be a simple, efficient \(uses less resources due to one-at-time loading method vs loading all increments\) and a fast way to iterate through a range. 



