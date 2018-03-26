# User Functions

---

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
    name = name*2
    return name
print(name_upper('Frank'))
```

**With no return value:**

```py
def name_upper(name):
    <code>
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
print(divisable_by(900, 10))
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
print(divisable_by(900, 10))???
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

## Calling a Function

To call a function, you simply call the function name and pass in any needed arguments. If the function returns a variable, it is wise to call the function and direct the return value into a variable.

```py
# Lets print a name
print_name('SrA. Snuffy')
```

## Cmdline Arguments

Arguments can also be passed through the command line or terminal.

#### Old:

Avoid the older version. The new version works in both Python 2.7 and 3.x

```py
import sys

args = str(sys.argv)
print sys.argv[0]
for i in range(len(sys.argv)):
    print 'args[%d]: %s' % (i sys.argv[i])
```

#### New:

```py
import argparse

parser = argparse.ArgumentParser(description='This is a demo')
parser.add_argument('-i','--input',help='Input arg', required=True)
args = parser.parse_args()

print args.input
```

## Returning

With functions, you have the choice to return a variable. This is done so that the function becomes it's own local scope... keeping the global scope clean from any interference that the function may cause. If you want to bring a local function variable outside of the local scope... return a variable. With that said, returned values can be reassigned. If you find yourself having to return a ton of variables, either use a sequence or mapping object or split up the functionality into additional functions.

```py
def create_initials(first_name, last_name):
    initials = first_name[0].upper() + last_name[0].upper()
    return initials

initials = create_initials("jack", "black")
print initials
```

## Pass by Reference

Pass by Object Reference simply means that objects passed to the functions are referenced. This is technically what Python does by default. Since the objects are referenced, it can be easy to change the contents of that object; especially mutable objects.

```py
#Define the function
def append_one(li)
    li.append(1)

# Declare and set a variable
l = [0]
# Pass that variable by reference to the function append_one()
append_one(l)
print l

# Since the function acted on a mutable variable... the contents of the object were changed.
[0, 1]
```

**Practical Example**

The following code contains a bit of everything we have learned including some things we have not learned. This is a more robust and error/hack proof version of divisible\_by that we looked at above.

```py
"""
Checks a certain range of numbers to see if they can divide into a user specified num
"""
# Program main, runs at start of program
def launch():
    num = raw_input('What number would you like to check?')
    amount = raw_input('How many numbers do you want to check?')

    if isInt(num) == False or isInt(amount) == False:
        print "You must enter an integer"
        launch() 
    elif int(amount) < 0 or int(num) < 0:
        print "You must enter a number greater than 0"
        launch() 
    else:
        divisable_by(int(num), int(amount))

# Checks num divisable numbers up to amount or itself
def divisable_by(num, amount):
    i = 1.0
    while (num / i >= 1 and amount > 0):
        if num % i == 0:
            print '{} is divsable by {}'.format(int(num), int(i))
            amount -= 1
        i += 1

# Checks if string represents an int
def isInt(x):
    try:
        int(x) ###
        return True
    except ValueError:
        return False

launch()
```

## 



