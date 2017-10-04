### Sequence Objects: Lists

Lists are very similar to C arrays. Lists **are mutable and nestable**. They are not ordered! There is no variable length per say, aside from what the system itself can handle. In other words, lists are dynamically adjusted to fit their contents. Lists can be multidimensional and can contain elements of different types. You can create a list using \[\].

**List example:**

```py
>>> my_list = ['Hello World', 15, True, 'w']​
>>> nested_list = [['such', 'wow'], 5, [False, '15']]​
```

### Slicing Lists

Much like strings, you can slice lists. There are some differences though. Slicing only one element will return a substring. Whereas slicing a range of elements will return another list.

**Slicing One Element:**

```py
>>> my_list = ['apple', 'orange', 'cherry', 'strawberry']​
>>> my_list[3]​
'strawberry'​
>>> type(my_list[3])
<class 'str'>
>>> nested_list = [['apple', 'orange'], ['onion', 'pepper']]​
>>> nested_list[3] # ???​
```

**Slicing Multiple Elements**

```py
>>> my_list[0:2]
['apple', 'orange', 'cherry'] # outputs list
>>> type(my_list[0:2])
<class 'list'>


>>> nested_list[0][1]​
'orange'​
>>> nested_list[0][0:2]​
['apple', 'orange']​
>>> nested_list[0:2][1] # ???​
```



### Indexing Lists

index\(\) will output the index of an element that matches index\(\)s argument. index\(\) looks for strict matches. Overall, this is useful for finding the index of a specific item. For example:

```py
>>> my_list = ['Hello World', 15, True, 'w']​
>>> my_list.index(15)​
1​
>>> my_list.index('Hello')​
Traceback (most recent call last):………​
# index method looks for strict matches​
# useful for finding index of a specific item
```



