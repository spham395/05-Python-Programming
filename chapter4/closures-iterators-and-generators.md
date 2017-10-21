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

## Generators

Generators are also iterators \(iterators are not generators though\)

```py
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
 my_gen = yrange(10)
print my_gen
for i in my_gen:
    print(i)
```

**Note: **When functions return all state is lost, a yield preserves local state and returns a generator object.

**Review: **https://wiki.python.org/moin/Generators

