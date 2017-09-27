# Running Python

There are a couple of ways to execute Python code. One way is through the **Python Interpreter,** which allows for on the fly code testing and sandboxing. The Python Interpreter uses **REPL:**

* **Read: **the user input
  * Some constructs like loops might be multiple lines
* **Evaluate: **the input
  * Attempt to perform the instruction
* **Print: **to the screen and
  * Print any requested info or an error with stack trace
* **Loop:**
  * Print the next prompt

The Python Interpreter can be launched from the command prompt or terminal using the following commands:

#### Linux & OS X

![](/assets/Screen Shot 2017-09-27 at 10.57.33 AM.png)

## Print

Python 3 replaced Python 2's print statement with a print function\(\). While Python 2 will be happy as is or with parantheses... Python 3 will throw an error if the parantheses are not included.

#### Python 2

```py
print 'Hello World!' # outputs: Hello World!
mystr = 'Goodbye World!'

print mystr # outputs: Goodbye World!
print("This works too") # This works too!
```

#### Python 3

```py
print("Hello World!") # Hello World!
mystr = 'Goodbye World!'

print(mystr) # Goodbye World!
```

## Integer Division

Python 2 treats numbers without a decimal as integers, whereas Python 3 will treat them as float if it applies. Python 2 Division with integers truncate the remainder! Setting one number as a real number will yield the correct result.

#### Python 2

```py
print 3/2 # 1
print 3.0/2 # 1.5
```

#### Python 3

```py
print 3/2 # 1.5
```

## Other Major Differences

#### Unicode:

Python 2 has ASCII **str\(\) **type, separate **unicode\(\) **type.. but no **byte** type.

Python 3 has Unicode \(**utf-8\)** **str **ings and two byte classes: **byte and bytearray. **

We will cover both in later lectures.

#### Input\(\) vs raw\_input\(\):

* Python 3 **input\(\)** always stores userinput as **str **objects. This is good.
* Python 2 **input\(\)** on the other hand fully evaluates the code the user gives it. **This is dangerous! **This gives the full power of Python to the user... and can be used in a malicious way. Instead, we use **raw\_input\(\) **in Python 2... which converts user input to a string. 

There are more differences between the two major releases. It's encouraged to look up the differences for better understanding.

