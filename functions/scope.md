# Scope

Scope refers to the visibility of variables. To be more clear, what parts of your program see what variables. In Python, we use **LEGB Rule:**

![](/assets/scope_resolution_1.png)

#### Local:

* Defined in the local scope of functions

```py
def sales_tax(amount):
    rate = 0.0625 # Local
    tax_total = amount * rate
    total = tax_total + amount
    print total

# Call function and pass parameter
sales_tax(200)
print tax_total #???
```

#### Enclosing-Function Global

* Refers to variables defined within local scope of functions wrapping other functions

```py
def program():
    amount = 200 # Enclosing-Function Global
    def sales_tax():
        rate = 0.0625
        tax_total = amount * rate
        total = tax_total + amount
        print total
    sales_tax()
program()
```

#### Global/Module

* Variables defined at the top level of files and modules

```py
amount = 200 #Global variable

def sales_tax():
    rate = 0.0625
    tax_total = amount * rate
    total = tax_total + amount
    print total

# Did not pass parameters
sales_tax()
```

#### Built-In

* Loaded into scope when interpreter starts up. \(Ex: hash\(\), min\(\), dict\(\), print\(\), etc\)



