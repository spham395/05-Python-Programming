# List Comprehension

This section is going to go over a bit more list comprehension. Analyze the following code snippets... they all do the same exact thing but in different ways. 

**Example 1:**

```py
a_list = [1, 2, 3, 4, 5]

def square_list(a_list):
    a = []
    for item in a_list:
        a.append(item*item)
    return a

print square_list(a_list)
```

**Example 2:**

```py
a_list = [1, 2, 3, 4, 5]

def square_list(a_list):
    for i in range(len(a_list)):
        a_list[i] *= a_list[i]
square_list(a_list)
print a_list
```

**Example 4:**

```py
a_list = [1, 2, 3, 4, 5]

def square_list(a_list):
    return [x*x for x in a_list]

print square_list(a_list)
```

**Example 5:**

```py
a_list = [1, 2, 3, 4, 5]

def square_list(a_list):
    return [x*x for x in a_list if x % 2 == 0]
 print square_list(a_list)
```



