# User Functions

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

Parameters are defined within the parentheses; they are undefined variables that you want to use within the function. This keeps the global scope clean \(we will learn more about this coming up\). You pass arguments \(defined variables\) on the function call. As shown below:

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

## Calling a Function

To call a function, you simply call the function name and pass in any needed arguments. If the function returns a variable, it is wise to call the function and direct the return value into a variable.

```py
# Lets print a name
print_name('SrA. Snuffy')
'SrA. Snuffy'#
```

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



