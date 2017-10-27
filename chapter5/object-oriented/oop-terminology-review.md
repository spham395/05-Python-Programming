# OOP Terminology Review

* **Class**
* * "Classes provide a means of bundling data and functionality together. Creating a new class creates a new
    \_type \_of object, allowing new \_instances \_of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods \(defined by its class\) for modifying its state."
* **Class Variable**
* * Variables defined within the class definition that belong to the class. These variables are shared to all instances of the class. 

  ```py
  class TestClass:
      i = 10

  print TestClass.i
  ```
* **Function/Method Overloading**

* * Function Overloading is the ability to create multiple functions with the same name. This allows us to pass different parameters. In Python, this is not needed. Instead... we can set default and optional parameters. 

  ```py
  def someFunc(x, y, x = None):
      if z is None:
          # Set a default for x or don't use it
      else:
          # Set and use all three

  someFunc(1,2)
  someFunc(1,2,3)
  ```
* **Instance Variable**
* * Similar to Class Variables... except they are only accessible to that one instance. These generally start with the 'self' keyword. 

  ```py
  class NameClass:
      def __init__(self, name):
          self.name = name

  dis_class =  NameClass('your_name')
  print dis_class.name
  #OUTPUT:
  'dis_name'
  ```
* **Inheritance**
* * A term used in OOP meaning that classes can inherit from other classes. 
* **Instance**
* * Means to create a instance or copy of a class. 
* **Instantiation**
* * Instantiation is the act of creating an object instance from a class.
* **Method**
* * A method is similar to a function but is associated with an object. Methods always take a class instance \(almost always 'self'\) as their first parameter. 
* **Object**
* * Everything in Python is an object. An object can be assigned to a variable or passed into a function as a argument. 
* **Operator Overloading**
* * Operator Overloading is the ability to change the meaning of an operator

  ```py

  ```



