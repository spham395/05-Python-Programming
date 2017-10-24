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
def divisable_by(num, amount = 5):
    i = 1.0
    while (num / i >= 1 and amount > 0):
        if num % i == 0:
            print "{} divided by {} equals: {}".format(num, i, num / i)
            amount -= 1
        i += 1
```

**Safe Way**

This forces the default arguments to be evaluated each time the function is called. This is especially important with mutable default objects.

```py
# Checks all numbers that can be divided into num... up until amount has been reached or we reach divide by self
def divisable_by(num, amount=None):
    if amount is None:
        amount = 5

    i = 1.0
    while (num / i >= 1 and amount > 0):
        if num % i == 0:
            print "{} divided by {} equals: {}".format(num, i, num / i)
            amount -= 1
        i += 1
```

#### Arguments

Arguments are defined variables that you pass on the function call.

**Examples of parameters and arguments:**

```py
def sales_tax(amount): # function and parameter 'amount'
    rate = 0.0625
    tax_total = amount * rate
    total = tax_total + amount
    print total

sales_tax(200) # Function call and argument 200
```

##### \*args and \*\*kwargs

* \*args are used to pass a non-keyworded, variable-length argument list
* \*\*kwargs is used to pass a keyworded, variable-length argument list
* kwargs are placed in dictionaries

**Example:**

```py
def my_func1(*args):
    for arg in args:
        print 'arg: ', arg
        print type(args)
def my_func2(**kwargs):
    for key, value in kwargs.iteritems():
        print key, value
my_func1('two', 3, 'four', 5)
my_func2(a=12, b = 'abc')
```

# Calling a Function

To call a function, you simply call the function name and pass in any needed arguments. If the function returns a variable, it is wise to call the function and direct the return value into a variable. 

```py
# Lets print a name
print_name('SrA. Snuffy')
```



