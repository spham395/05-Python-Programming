# Sequence Objects: Lists

Lists are very similar to C arrays. Lists **are mutable and nestable**. They are not ordered! There is no variable length per say, aside from what the system itself can handle. In other words, lists are dynamically adjusted to fit their contents. Lists can be multidimensional and can contain elements of different types. You can create a list using \[\].

**List example:**

```py
>>> my_list = ['Hello World', 15, True, 'w']​
>>> nested_list = [['such', 'wow'], 5, [False, '15']]​
```

### 

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

#### In/not in Operator

Works just like index\(\).

```py
>>> True in my_list​
True​
>>> 'Hello' in my_list​
False​
>>> 20 not in my_list​
True
```

### Modifying Lists

Remember, lists are **MUTABLE!** This simply means we can modify it in place via appending, removing, combining, etc.

#### Updating Lists:

* append\(\)

* * Adds onto the end of the list​
* change index \(ex: list\[i\]\)​

* * Changes the specified index​
* insert\(i,x\)​

* * inserts object x into the list at offset indexi\)​
* sort, sorted\(\)​

* * Sorts list alphabetically​
* * Both accept a reverse parameter with a Boolean value​
* * Both also accept a key parameter that specifies a function to be called on each list element prior to making comparisons.​

**Example:**

```py
>>> my_list = [1,2,3,4,5]​
>>> my_list.append(6)​
[1, 2, 3, 4, 5, 6]​
>>> my_list[0] = 99​
>>> my_list​
[99, 2, 3, 4, 5, 6]​
>>> my_list.insert(0, 1)​
>>> my_list​
[1, 99, 2, 3, 4, 5, 6]​
>>> messy_list = [2,1,4,5,3,5,100,222,44]​
>>> sorted(messy_list)​
# ??????​
>>> messy_list.sort(reverse=True)​
>>> messy_list​
# ??????​
```

#### 

#### Combining Lists:

* extend\(\)​

* * concatenates the first list with another list or iterable.​
* +=​

* * also concatenates the first list with another list or iterable.​

**Example:**

```py
>>> rally_cars = ['Subaru', 'Ford’]​
>>> rally_cars.extend(['Mini', 'Audi'])​
>>> rally_cars​
['Subaru', 'Ford', 'Mini', 'Audi']​
>>> rally_cars += ['Peugeot', 'MG Metro']​
>>> rally_cars​
['Subaru', 'Ford', 'Mini', 'Audi', 'Peugeot', 'MG Metro']​
​
```

#### Removing List Elements:

* list.remove\(x\)​

* * Removes the first value that matches x.​
* del list\[x\]​

* * Removes a specific index.​
* list.pop\(x\)​

* * Removes the specific index and returns the removed element.​

**Example:**

```py
# remove()​
>>> my_list = [1,2,3,3,4,5]​
>>> my_list.remove(3)​
>>> my_list​
[1, 2, 3, 4, 5]​
# del​
>>> del my_list[2]​
>>> my_list​
[1, 2, 4, 5]​
# pop()​
>>> my_list.pop(1)​
2 # value popped​
>>> my_list​
[1, 4, 5]​
```



