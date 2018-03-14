# List Comprehension

Python supports something called "list comprehension". In short, this allows us to write minimal, easy and readable lists in a way like mathematicans do.

![](/assets/Screen Shot 2017-10-20 at 9.29.38 PM.png)

**Normal List**

```py
a_list = [1,2,3,4,5]

def square_list(a_list):
    a = []
    for item in a_list:
        a.append(item*item)
    return a

    print square_list(a_list)

# Output
[1, 4, 9, 16, 25]
```

**Normal List with Refactoring**

###### \(In this example the a\_list global variable was overwritten. This can be avoided by reassigning the results to a new variable.\)

```py
a_list = [1,2,3,4,5]

def square_list(a_list):
    for i in range(len(a_list)):
        a_list[i] *= a_list[i]

square_list(a_list)
print a_list

# Output
[1, 4, 9, 16, 25]
```

**List Comprehension Without Conditional**

```py
a_list = [1,2,3,4,5]

def square_list(a_list):
    return [x*x for x in a_list]

print square_list(a_list)

#Output 
[1, 4, 9, 16, 25]
```

**List Comprehension With Conditional**

```py
a_list = [1,2,3,4,5]

def square_list(a_list):
    return [x*x for x in a_list if x % 2 == 0]

print square_list(a_list)

# Output
[4, 16]
```

**Set Comprehension With Conditional**

```py
a_list = [1,2,3,4,5]

def square_list(a_list):
    return {x*x for x in a_list if x % 2 == 0}

print square_list(a_list)

# Output
set([16, 4])
```



