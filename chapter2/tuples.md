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



