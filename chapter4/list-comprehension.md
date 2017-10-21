# List Comprehension

This section is going to go over a bit more list comprehension. Analyze the following code snippets... do not copy the code and run it. Try to figure out what the code does to the lists.

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



