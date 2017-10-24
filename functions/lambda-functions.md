# Lambda Functions

It's best to start off with some examples:

**Example 1:**

```py
my_list = range(26)
print(filter(lambda x: x % 2 == 0, my_list))
```

**Example 2:**

```py
g = lambda x,y: x>y
print g(1,2)
print g(2,1)
```

As you can tell, lambdas appear to be shortened functions; specifically one lined functions. And while this is true to an extent... that is not their purpose. Nor are Lambdas like C/C++ inline statements... used for performance reasons.

Lambdas, in short, are anonymous functions. Functions without a name. They are generally passed as arguments to higher-order functions as well as a variety of other uses. Below are some of the features of a Lambda

**Lambda Features:**

* Lambda forms can take any number of arguments

* Return only one value in the form of an expression

* They cannot contain commands or multiple expressions

* It cannot be a direct call to print because lambda requires an expression

* Lambda functions have their own namespace

Due to the fact that they have their own local namespace... Lambdas cannot access variables other than those in their parameters list and globals.

#### **Breakdown of a Lambda**

```py
#Define a regular function
def reg_function(x):
    return x**2

# Make it one line
def reg_function(x): return x**2

# Turn it into a lambda
new_stuff = lambda x: x**2
```

## Lab 4A: Calculator

Create a fully functional calculator using BOTH functions and lambdas. Create a user menu as well as a "screen" where the numbers and operations take place. The calculator needs to have the following functionality:

* Addition
* Subtraction
* Division
* Multiplication
* Power

Additional Features:

* More than two numbers
* Continuous operations \(5 + 5 + 2 - 1 / 2 for example\)
* Additional operations
* etc



