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

* * Function Overloading is the ability to create multiple functions with the same name. This allows us to pass different parameters. In Python, this is generally not needed. Instead... we can set default and optional parameters. 

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
* * Similar to Class Variables... except they are only accessible to that one instance. These generally start with the 'self' keyword and are contained within methods. 

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
* * A term used in OOP meaning that classes can inherit from other classes. In other words, it's the transfer of characteristics from one class to another class/classes that are derived from it. 
* **Instance**
* * An individual object of a certain class. 
* **Instantiation**
* * Instantiation is the act of creating an object instance from a class.
* **Method**
* * A method is similar to a function but is associated with an object. Methods always take a class instance \(almost always 'self'\) as their first parameter. 
* **Object**
* * Everything in Python is an object. An object can be assigned to a variable or passed into a function as a argument. It's a unique data structure that's defined by it's class. 
* **Operator Overloading**
* * Operator Overloading is the ability to change the meaning of an operator. This is often done by assigning more than one function to a particular operator. 



