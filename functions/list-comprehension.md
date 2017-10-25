# List Comprehension

Python supports something called "list comprehension". In short, this allows us to write minimal, easy and readable lists in a way like mathematicans do. 

**Normal List Comprehension**

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

**First Level of Refactoring**

In this example... we actually overwrote the global a\_list variable by accident. It is important you pay attention to this and try to avoid this mistake in the future. 

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

**Second Level of Refactoring**

```py
a_list = [1,2,3,4,5]

def square_list(a_list):
    return [x*x for x in a_list]
    
print square_list(a_list)

#Output 
[1, 4, 9, 16, 25]
```

**Third Level of Refactoring With Even Condition**

```py
a_list = [1,2,3,4,5]

def square_list(a_list):
    return [x*x for x in a_list if x % 2 == 0]
    
print square_list(a_list)

# Output
[4, 16]
```

**Final Level of Refactoring with Even Condition**

```py
a_list = [1,2,3,4,5]

def square_list(a_list):
    return {x*x for x in a_list if x % 2 == 0}
    
print square_list(a_list)

# Output

```



