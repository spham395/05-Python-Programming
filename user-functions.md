# User Functions

Python functions are blocks of reuseable code that can be called to accomplish some sort of functionality. Functions are meant to split up the code into functionally organized code that can be reused. In Python, you do not have to return a value.

To define a function use: **def function\_name\(parameters\):**

```py
def function_name(parameters):
    x = 0 # What we want to return

    return x # What we return
```

**With return value:**

```py
def name_upper(name):
    return name
```

**With no return value:**

```py
def name_upper(name):
    print name
```

**Another example:**

```py
def divisable_by(num, amount):
    i = 1.0
    while (num / i >= 1 and amount > 0):
        if num % i == 0:
            print "{} divided by {} equals: {}".format(num, i, num / i)
            amount -= 1
        i += 1
```

## Parameters and Arguments

#### Parameters

Parameters are defined within the parentheses; they are undefined variables that you want to use within the function. This keeps the global scope clean. We can specify default parameter values as well as specify type. A lot of this can be done within the parentheses... but this can lead to unexpected problems.

**Common Way \(but risky\)**

```py
def
```



