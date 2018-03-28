# User Classes

---

Classes are used to create objects that bundle data and functionality together. With this, classes are highly reusable, cleaner and more efficient. Here are some considerations:

**Keywords**

Reserved words of the language, and cannot be used as ordinary identifiers. They must be spelled exactly as written here:

```
and       del       from      not       while    
as        elif      global    or        with     
assert    else      if        pass      yield    
break     except    import    print     
class     exec      in        raise              
continue  finally   is        return             
def       for       lambda    try
```

To verify that a string is a keyword you can use [`keyword.iskeyword`](https://docs.python.org/3/library/keyword.html#keyword.iskeyword); to get the list of reserved keywords you can use [`keyword.kwlist`](https://docs.python.org/3/library/keyword.html#keyword.kwlist):

```
>>> import keyword
>>> keyword.iskeyword('break')
True
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 
 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
 'while', 'with', 'yield']
```

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
* Name classes using CapWords convention \(camel-case\)
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

### Function vs Method

A **function **is a piece of code that is called by name. It can be passed data to operate on \(i.e., the parameters\) and can optionally return data \(the return value\). All data that is passed to a function is explicitly passed.

```
def sum(num1, num2):
    return num1 + num2
```

A **method **is a piece of code that is called by name that is associated with an object. In most respects it is identical to a function except for two key differences.

1. It is implicitly passed for the object for which it was called.
2. It is able to operate on data that is contained within the class \(remembering that an object is an instance of a class - the class is the definition, the object is an instance of that data\).

```
class Dog:
    def my_method(self):
        print "I am a Dog"

dog = Dog()
dog.my_method()  # Prints "I am a Dog"
```



