# User Functions

Python functions are block of reusable code that can be called by reference. Functions are meant to split up the code into functionally organized code that can be reused. In Python, you do not have to return a value.

To define a function use: **def function\_name\(parameters\):**

```py
def function_name(parameters):​
    x = 0​
​
    return x
```



### Parameters

Parameters are defined within the parentheses; they are variables that you want to use within the function. This keeps the global scope clean \(we will learn more about this coming up\). 

```py
def sales_tax(amount):​
    rate = 0.0625​
    tax_total = amount * rate​
    total = tax_total + amount​
    print total​
​
# Call function and pass argument
sales_tax(200)​
```



