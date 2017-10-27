# User Classes

* **Classes are used to create objects that bundle data and functionality together.**
* **Classes provide highly reusable code in a cleaner, more efficient matter.**
* **We won't hash the fundamentals of Object Oriented Programming too hard since Python and C++ OOP are very similar. But some considerations:**
* * Python is typically 5-10x shorter than C++ equivalent
  * Python programs run slower than C++ at runtime
  * There isn't a protected, public or private keyword per-say
  * Python is better as a "glue" program or for fast implementations. Thus why we use Python in socket programing for example

### Creating an Instance in a Different File

```py
from MyClass import MyClass

 x = MyClass(name = "Iron Man")
print x.getName()
```

### Inheriting From a Parent Class

**Parent Class**![](/assets/Screen Shot 2017-10-27 at 1.28.06 AM.png)

**Child Class**

![](/assets/Screen Shot 2017-10-27 at 1.29.34 AM.png)

**Example Call**

```py
from USResident import USResident

 # pass init attributes. Must include additional attribute for status
resident = USResident("Joe Smo", "citizen")
resident.setAge(23) # Set age to 23

 print "{} is a {} and is {} years of age".format(resident.getLastName(), 
resident.getStatus(), resident.getAge())
```



