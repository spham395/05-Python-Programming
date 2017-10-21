# Closures, Iterators and Generators

## Closures

No. We aren't talking about the programming language Clojure. A Closure is a function object that remembers values in enclosing scopes regardless of whether those scopes are still present in memory. If you have written a function that returned another function, you probably have used closures without even knowing.

**Example:**

```py
def generate_power_func(n):
    def nth_powah(x):
        return x**n
    return nth_powah
 print generate_power_func(10)

# What happens?
```

## Iterators

An iterator is just an object with a state that remembers where it is during iteration. Iterable objects can range from while loops to the actual iterator object. \#\#\#\# Finish 

