# User Classes

* **Classes are used to create objects that bundle data and functionality together.**
* **Classes provide highly reusable code in a cleaner, more efficient matter.**
* **We won’t hash the fundamentals of Object Oriented Programming too hard since Python and C++ OOP are very similar. But some considerations:**
* * Python is typically 5-10x shorter than C++ equivalent
  * Python programs run slower than C++ at runtime
  * There isn’t a protected, public or private keyword per-say
  * Python is better as a “glue” program or for fast implementations. Thus why we use Python in socket programing for example

#### Python Specific

* \_\_init\_\_ \(Constructor\)
* \_\_del\_\_ \(Destructor\)
* It's best to name the Python file after the class name. 
* class ClassName\(object\):
   --to define class
* Name classes using CapWords convention
* Variables defined under classes are shared through all instances
* Variables defined in methods are only for a single instance
* When creating methods, the first parameter must be self. \(similar to “this” in other languages\)
* A “private” member can be created by prepending a double underscore \(only prepend\) to the name. It will not be visible outside of the class.  **\_\_example**
* Inheritance, multiple inheritance and polymorphism are all supported.
* Create instance of class, do not need to pass “self” even though it is in the \_\_init\_\_definition
* var.attrib = value is the common way to interact\(dot notation\)
* getattr, hasattr, setattr, delattr exist for manipulating attributes as well
* built in: \_\_dict\_\_, \_\_doc\_\_, \_\_name\_\_, \_\_module\_\_, \_\_bases\_\_
* overloadable: \_\_init\_\_, \_\_del\_\_, \_\_repr\_\_, \_\_str\_\_, \_\_cmp\_\_
* **Dir\(\), type\(\), isinstance\(\) built in functions**

**Once again, Python doesn’t really have public, protected or private. A single “\_” prefix indicates internal usage. “\_\_” double hides attribute name**

### Composition vs Inheritance

* **Best advice is composition over inheritance, but use inheritance when needed.**
* **Inheritance can complicate things \(especially multiple inheritance\) and make larger projects confusing**
* **Namespace collisions are a major problem in inheritance**
* **Time must be given to design to effectively use inheritance, which could be time used to stand up composition quicker.**

### Creating an Instance in a Different File

```py
from MyClass import MyClass

 x = MyClass(name = "Iron Man")
print x.getName()
```



