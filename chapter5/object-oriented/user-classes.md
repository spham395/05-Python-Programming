# User Classes

---

Classes are used to create objects that bundle data and functionality together. With this, classes are highly reusable, cleaner and more efficient. Here are some considerations:

* Python is typically 5-10x shorter than C++
* There isn't a protected, public or private keyword per-say. 
* Python is better as a "glue" program or for fast implementations. Thus why we use Python in socket programming for example.

### Creating an Instance in a Different File

```py
from MyClass import MyClass

x = MyClass(name = "Iron Man")
print x.getName()
```

## Python Specific

```
__init__ (Constructor)
__del__ (Deconstructor)
```

* It's best to name the Python file after the class name/vise-versa.
* class ClassName\(object\): -- to define class
* Name classes using CapWords convention
* Variables defined under classes are shared though all instances
* Variables defined in methods are only for a single instance
* When creating methods, the first parameter must be self. \(similar to "this" in other languages\)
* A "private" member can be created by prepending a double underscore \(only prepend\) to the name. It will not be visable outside of the class. \_\_example
* Inheritance, multiple inheritance and polymorphism are all supported
* var.attrib = value is the common way to interact\(dot notation\)
* getattr, hasattr, setattr, delattr exist for manipulating attributes as well
* built in: 

```py
__dict__, __doc__, __name__, __module__, __bases__
```

* Overloadable:

```py
__init__, __del__, __repr__, __str__, __cmp__
```

* dir\(\), type\(\), isinstance\(\) are built in functions
* Once again, Python doesn't really have public, protected or private. A single _"\_" prefix indicates internal usage. "\__\_" hides attributes name. 

## Composition vs Inheritance

* Best advice is composition over inheritance, but use inheritance when needed. 
* Inheritance can complete things \(especially multiple inheritance\) and make larger projects confusing
* Namespace collisions are a major problem in inheritance
* Time must be given to design to effectively use inheritance, which could be time used used to stand up composition quicker. 

**Parent Class**![](/assets/Screen Shot 2017-10-27 at 1.28.06 AM.png)

**Child Class**

![](/assets/Screen Shot 2017-10-27 at 1.29.34 AM.png)

**Example Call**

```py
from USResident import USResident
# pass init arguments. Must include additional argument for status
resident = USResident("Joe Smo", "citizen")
resident.setAge(23)

print "{} is a {} and is {} years of age.".format(resident.getLastName(), resident.getStatus(), resident.getAge())
```

### Bonus Lab: _Janken Pon!_

Create a game of Rock, Paper, Scissors using classes.

