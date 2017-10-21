User Functions

Python functions are block of reusable code that can be called to accomplish some sort of functionality. Functions are meant to split up the code into functionally organized code that can be reused. In Python, you do not have to return a value.

To define a function use: **def function\_name\(parameters\):**

```py
def function_name(parameters):​
    x = 0​ # What we want to return
​
    return x # What we return
```

**With Return Value:**

```
def name_upper(name):
```

**No return value:**

```py
def print_name(name):
    print name
```

**Another Example:**

```py
def divisable_by(num, amount):
    i = 1
    while (num / i != 1):
        print num / i
        i += 1
```

## Parameters and Arguments

#### Parameters

Parameters are defined within the parentheses; they are undefined variables that you want to use within the function. This keeps the global scope clean.

#### Arguments

Arguments are defined variables that you pass on the function call.

**Example of Parameters and Arguments:**

* **\*\*kwargs is used to pass a keyworded, variable-length argument list**

```py
def sales_tax(amount):​ # function and parameter amount
    rate = 0.0625​
    tax_total = amount * rate​
    total = tax_total + amount​
    print total​
​
# Call function and pass argument
sales_tax(200)​ # function call and argument 200
```

#### \*args and \*\*kwargs

* \*args is used to pass a non-keyworded, variable-length argument list

* \*\*kwargs is used to pass a keyworded, variable-length argument list

* Arguments passed in with t meos are placed in a dict

**Example:**

```py
def my_func1(*args):
    for arg in args:
        print 'arg: ', arg
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
'SrA. Snuffy'#
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

Pass by Object Reference simply means that objects passed to the functions are referenced. This is technically what Python does by default. Since the objects are referenced, it can be easy to change the contents of that object. Remember, everything in Python is an object!

```py
# Define the function
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

#### 

#### 

#### Practical Example

The following code contains function calls in the Global and Enclosing-Function Global scopes. There is also error handling, which we will cover later.

```py
"""
Checks a certain range of numbers to see if they can divide into a user specified num
"""
def divisable_by(num, amount):
    i = 1.0
    # Stop num / i when we reach num / num... regardless of amount
    while (num / i != 1.0 and num / i != -1.0):
        if (i == amount + 1):
            break
        elif (num % i == 0):
            print '{} is divsable by {}'.format(int(num), int(i))
        else:
            print '{} is NOT divsable by {}'.format(int(num), int(i))
        i += 1.0
    else:
        print '{num} is divisable by {num}'.format(num = num)

# Program main, runs at start of program
def launch():
    num = raw_input('What number would you like to check?')
    amount = raw_input('How many numbers do you want to check?')

    if isInt(num) == False or isInt(amount) == False:
        print "You must enter an integer"
        launch() ### Enclosing-Function Global
    elif int(amount) < 0:
        print "You must enter a number greater than 1"
        launch() ### Enclosing-Function Global
    else:
        divisable_by(int(num), int(amount)) ### Enclosing-Function Global

# Checks if string represents an int
def isInt(x):
    try:
        int(x) ### 
        return True
    except ValueError:
        return False

launch()
```

#### 



