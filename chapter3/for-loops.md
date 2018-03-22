# For Loops

---

#### For Loop in C:

```c
char *my_string = "Python";
for (int i = 0; i < strlen(my_string); i++) {
    printf(%c\n", my_string[i]);
}
```

#### Python in C Style:

```py
my_string = "Python"
for i in range(len(my_string)):
    print(my_string[i])
```

While the Python one certainly is shorter and looks cleaner... it's still not Pythonic. It's ugly and not the most readable code.

#### For Loop... Python Style

```py
my_string = "Python"
for letter in my_string:
    print letter
```

So easy, a caveman can do it! But, how does this happen under the hood?

Remember Data Types chapter? Strings are iterable just like in C. The "in" operator simply calculates the count of my\_string and iterates through it as var letter. The value of letter is my\_string\[i\].

## For Looping Dictionaries

```py
for key, value in dict.iteritems():
    pass
```

```py
x = {'stu1':'James', 'stu2':'Bob', 'stu3':'Rengar'}

for stu_id, name in x.iteritems():
    print "{}'s name is {}".format(stu_id, name)
```

---

### Lab 3E: Fibonacci \(Iterative vs Recursive\)

Write one function that prints out the first 100 numbers in the Fibonacci sequence iteratively and one recursively.

![](/assets/13import.png)

![](/assets/14import.png)

