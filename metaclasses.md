# Metaclasses

---

![](/assets/QQ0OK.png)

**Defined as “the class of a class”.**

* Any class whose instances are themselves classes.
* type is a metaclass for instance; it creates classes!
* Used to construct classes. \(always happens under hood\)
* Can create dynamic classes with less lines using type.
* Think: instances are to classes as classes are to metaclasses.
* To create a metaclass, create a class that inherits from type

```
# in the most simple form
class Meta(type):
    pass
```

* Classes are normally created with the type metaclass
* We can create a class with a different metaclass:

```
# Python 2
class Final(object):
    __metaclass__ = Meta
# Python 3
class Final(metaclass=Meta):
    pass
```

**Example:**

```
class Meta(type):
    def __init__(cls, name, bases, dct):
        print "Creating class {} using Meta".format(name)
        super(Meta, cls).__init__(name, bases, dct)
class Foo(object):
    __metaclass__ = Meta
class FooBar(Foo):
    pass
```

First we create a new metaclass called **Meta**:

* On the construction of classes built using Meta, we print out that we are creating a class using Meta.

Next, create a class called Foo… built from Meta rather than type.

Finally, create a FooBar class from Foo.

* Notice how it too was built using Meta?



