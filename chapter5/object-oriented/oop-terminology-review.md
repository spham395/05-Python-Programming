# OOP Terminology Review

---

**Attribute**

* Values associated with an individual object. Attributes are accessed using the 'dot syntax':

```
a.x means fetch the x attribute from the 'a' object.
```

**Argument**

* ```
  Extra information which the computer uses to perform commands.
  ```

**Class**

* A template for creating user-defined objects. Class definitions normally contain method definitions that operate on instances of the class.

* Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods \(defined by its class\) for modifying its state.

**Class Variable**

* Variables defined within the class definition that belong to the class. These variables are shared to all instances of the class.

  ```py
  class TestClass:
      i = 10

  print TestClass.i
  ```

**Constructors**

* Fuctions that are automatically called when you create a new instance of a class.

**Conditional Statement**

* Statement that contains an "if" or "if/else".

**Deconstructor**

**def**

* Defines a function or method

**Debugging**

* The process of finding and removing programming errors.

**Function**

* A parameterized sequence of statements.

###### **Syntax**

```
def function_name(parameters, named_default_parameter=value):
  # Some code here
```

**Function/Method Overloading**

* Function Overloading is the ability to create multiple functions with the same name. This allows us to pass different parameters. In Python, this is generally not needed. Instead... we can set default and optional parameters.

  ```py
  def someFunc(x, y, z = None):
      if z is None:
          # Set a default for z or don't use it
      else:
          # Set and use all three

  someFunc(1,2)
  someFunc(1,2,3)
  ```

**Immutable**

* An object with fixed value. Immutable objects include numbers, strings and tuples.

**Inheritance**

* A term used in OOP meaning that classes can inherit from other classes. In other words, it's the transfer of characteristics from one class to another class/classes that are derived from it. 

Initialization



**Instance**

* An individual object of a certain class. 

**Instance Variable**

* Similar to Class Variables... except they are only accessible to that one instance. These generally start with the 'self' keyword and are contained within methods.

  ```py
  class NameClass:
      def __init__(self, name):
          self.name = name

  dis_class =  NameClass('your_name')
  print dis_class.name
  #OUTPUT:
  'dis_name'
  ```

**Instantiation**

* Instantiation is the act of creating an object instance from a class.

**Lambda**

* A shorthand to create anonymous functions.

Library

Magic Method

**Method**

* Methods are functions that are called using the attribute notation. There are two flavors: built-in methods \(such as append\(\) on lists\) and class instance methods. A method is similar to a function but is associated with an object.

Module

**Namespace**

* The place where a variable is stored in a Python program's memory. Namespaces are implemented as a dictionary. There are the local, global and builtins namespaces and the nested namespaces in objects \(in methods\).

**Object**

* Everything in Python is an object. An object can be assigned to a variable or passed into a function as a argument. It's a unique data structure that's defined by it's class. Any data with state \(attributes or value\) and defined behavior \(methods\).

**Operator Overloading**

* Operator Overloading is the ability to change the meaning of an operator. This is often done by assigning more than one function to a particular operator.

Package

Parameter

**Self**

* Represents the instance of the class. By using the "_self_" keyword we can access the _attributes_ and _methods_ of the class in python.



**Value**

* Placeholder for texts and numbers. The equal sign \(=\) is used to assign values to variables.

Variable



---

### Bonus Lab: _Janken Pon!_

Create a game of Rock, Paper, Scissors using classes.

