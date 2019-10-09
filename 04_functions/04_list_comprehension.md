|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## List Comprehension

Python supports something called "list comprehension". In short, this allows us to write minimal, easy and readable lists in a way like mathematicans do. Essentially you put everything in a one liner. 

![](/assets/SS-9.29.38.png)

### Steps

Taking a look at the example above, let's break it down into something more understandable.

* First, the _for e in a\_list_ is examined. 
  * **a\_list** is just some var list that is visable within our scope
  * We are going to iterate through this list...
* While itterating through the list, we are going to check the **optional predicate**, _if type\(e\) == types.IntType_ in this case
  * So per iteration, we check that condition. If it's true, we execute the output expression...
  * As per the name, it's optional. If there is no optional predicate, the output expression simply runs. 
* The **output expression**, e\*\*2 in this case, is ran if the optional predicate exists and is True. 
  * This happens per iteration of a\_list as well. 

**Normal List**

```python
a_list = [1,2,3,4,5]

def square_list(a_list):
    a = []
    for item in a_list:
        a.append(item*item)
    return a

print(square_list(a_list))

# Output
[1, 4, 9, 16, 25]
```

**Normal List with Refactoring** 

### \(In this example the a\_list global variable was overwritten. This can be avoided by reassigning the results to a new variable.\)

```python
a_list = [1,2,3,4,5]

def square_list(a_list):
    for i in range(len(a_list)):
        a_list[i] *= a_list[i]

square_list(a_list)
print(a_list)

# Output
[1, 4, 9, 16, 25]
```

**List Comprehension Without Conditional**

```python
a_list = [1,2,3,4,5]

def square_list(a_list):
    return [x*x for x in a_list]

print(square_list(a_list))

#Output 
[1, 4, 9, 16, 25]
```

**List Comprehension With Conditional**

```python
a_list = [1,2,3,4,5]

def square_list(a_list):
    return [x*x for x in a_list if x % 2 == 0]

print(square_list(a_list))

# Output
[4, 16]
```

**Set Comprehension With Conditional**  

Instead of using brackets \[ \] as you would for lists you use curly braces \{ \} like you would for a set.

```python
a_list = [1,2,3,4,5]

def square_list(a_list):
    return {x*x for x in a_list if x % 2 == 0}

print(square_list(a_list))

# Output
set([16, 4])
```
If you are looking to get rid of duplicates within a list then using Set Comprehension is good for this. 

```python
# This list has duplicates
b_list = [1,2,2,3,4,4,5]

def square_list(b_list):
    return [x*x for x in b_list]

squared_list = square_list(b_list))
print(squared_list)
# We can convert this list to a set by using the set() method
set(squared_list)


# Why do the extra steps when we can just use set comprehension
def square_set(b_list)
    return {x*x for x in b_list}

squared_set = square_set(b_list))
print(squared_set)
```
**Dictionary Comprehension** 

Dictionary comprehension is a great way to take one dictionary and transform, or conditionally include items into a new dictionary. Just remember not to make these too complex. Their main purpose is to make your code more readable. 

```python
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }

squared_dict = {k:v*v for (k,v) in my_dict.items()}
print(squared_dict)
```
---

|[Next Topic](/04_functions/05_closures_iterators_generators.md)|
|---|
