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

* * inserts object x into the list at offset index i\)​
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

#### Map, Filter, Reduce:

**Map **applies a function to all the items in an input\_list.

```
map(function_to_apply, list_of_inputs)
```

**Example:**

```
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

**Map **allows us to implement this in a much simpler way.

```
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

```
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
```

**Filter ** - creates a list of elements for which a function returns true.

```
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]
```

 The filter resembles a for loop but it is a builtin function and faster.

**Reduce **-  performs some computation on a list and return the result.  It applies a rolling computation to sequential pairs of values in a list.

**Example: ** If you wanted to compute the product of a list of integers.

```
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24
```

Using reduce:

```
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24
```



