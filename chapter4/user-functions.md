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

#### Calling a Function

To call a function, you simply call the function name and pass in any needed arguments. If the function returns a variable, it is wise to call the function and direct the return value into a variable. 

```
# Using the functions above
# 
```

## 

## Parameters

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

## Scope

Scope refers to the visibility of variables. To be more clear, what parts of your program see what variables. In Python, we use **LEGB Rule:**

#### Local:

* Defined in the local scope of functions

```py
def sales_tax(amount):​
    rate = 0.0625​
    tax_total = amount * rate​
    total = tax_total + amount​
    print total​
​
# Call function and pass parameter​
sales_tax(200)​
print tax_total # ????​
```

#### Enclosing-Function Global

* Refers to variables defined within local scope of functions wrapping other functions.

```py
def program():​
    amount = 200​
    def sales_tax():​
        rate = 0.0625​
        tax_total = amount * rate​
        total = tax_total + amount​
        print total​
​
    sales_tax()​
program()​
```

#### Global/Module

* Variables defined at the top level of files and modules

```py
amount = 200 # Global Variable​
​
def sales_tax():​
    rate = 0.0625​
    tax_total = amount * rate​
    total = tax_total + amount​
    print total​
​
# Did not pass parameters​
sales_tax()​
```

#### Built-in

* Loaded into scope when interpreter starts up. \(Ex: hash\(\), min\(\), dict\(\), print\(\), etc\)



