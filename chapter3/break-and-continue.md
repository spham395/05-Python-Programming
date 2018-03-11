# Break and Continue

### Break

The break statement simply breaks out of the innermost enclosing loop.

```py
for i in xrange(1, 101):
    if i == 10:
        print "NEOW MORE LIVES!"
        break
    print i
```

**Output:**

```
1
2
3
4
5
6
7
8
9
NEOW MORE LIVES!
```

### Continue

The continue statement continues with the next iteration of the loop.

```py
for i in xrange(1, 100):​
    if i % 2 == 0:​
        print "{} is an even number!".format(i)​
        continue #prevents second print from running​
    print "{} is an odd number!".format(i) ​
```

**Output:**

```
1 is an odd number!
2 is an even number!
3 is an odd number!
4 is an even number!
5 is an odd number!
6 is an even number!
7 is an odd number!
8 is an even number!
9 is an odd number!
10 is an even number!
11 is an odd number!
12 is an even number!
13 is an odd number!
14 is an even number!
15 is an odd number!
16 is an even number!
17 is an odd number!
18 is an even number!
19 is an odd number!
20 is an even number!
....
```

Notice how the second print is skipped entirely for even numbers!

---

# Lab 3B FizzBuzz

---

Iterate through a loop 100 times… printing “Fizz” for any number dividable by 3 and “Buzz” for any number dividable by 5. If the number is dividable by both… print “FizzBuzz”. All other numbers… print the number.

```
​1​
2​
Fizz​
4​
Buzz​
Fizz​
7​
…​
14​
FizzBuzz​
…​
```



