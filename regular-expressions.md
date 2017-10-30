# Regular Expressions

Regular expressions, often referred to as REs or regexes, are bits of small and highly specialized programming language embedded inside Python. The PyDocs actually contains an entire page on how to use regex. We will be touching on some of it's functionality... it'll be up to you to utilize the PyDocs and take your knowledge to the next level.

**PyDocs HOWTO**

[https://docs.python.org/3/howto/regex.html](https://docs.python.org/3/howto/regex.html)

**PyDocs Re**

[https://docs.python.org/2/library/re.html](https://docs.python.org/2/library/re.html)

### Using Regular Expressions

**re.compile: **compiles regular expression into pattern objects which allows for repeated use

**re.match: **apply pattern to the start of string, return match or None

**re.search: **scan through string, return match or None

**re.findall: **find all matches and return them as a list

**Python re search and compile example:**

```py
import re

search_str = "This is a string to search"
re_search = re.compile("string")
matched_obj = re_search.search(search_str)

print matched_obj
```

```
<_sre.SRE_Match object at 0x02CBFA68>
```

**Practical Example**

```py
import re

patterns = ['Enterprise', 'Death Star']
pharse = "The Enterprise is the flagship of the Federation."

for pattern in patterns:
    print 'Looking for "{}" in "{}": '.format(pattern, pharse)

    if re.search(pattern, pharse):
        print "found a match!"
    else:
        print "no match!"
```

```
Looking for "Enterprise" in "The Enterprise is the flagship of the Federation.":
found a match!
Looking for "Death Star" in "The Enterprise is the flagship of the Federation.":
no match!
```

**Python re search start\(\) and end\(\):**

```py
import re

pattern = "Dave"
text = "I'm sorry Dave, I'm afarid I can't do that."

match = re.search(pattern, text)

start = match.start()
end = match.end()

print 'Found "{}" in "{}" from {} to {} ("{}")'.format(match.re.pattern, match.string, start, end, text[start:end])
```

```
Found "Dave" in "I'm sorry Dave, I'm afarid I can't do that." from 10 to 14 ("Dave")
```

**Python re match example:**

Python's re.match is similar to re.search. The main difference being that match searches only at the start of the string whereas search will apply the pattern to the entire string.

```py
import re

text = "I turned myself into a pickle. I'm Pickle Riiiiick"

match = re.match("I turned myself", text)
match2 = re.match("Picke", text)

if match == None:
    print 'Could not find "{}" in "{}"'.format(match.re.pattern, match.string)
else:
    print 'Found "{}" in "{}"'.format(match.re.pattern, match.string)

if match2 == None:
    print 'Cound not find "{}" in "{}"'.format(match.re.pattern, match.string)
else:
    print 'Found "{}" in "{}"'.format(match.re.pattern, match.string)
```

```
Found "I turned myself" in "I turned myself into a pickle. I'm Pickle Riiiiick"
Cound not find "I turned myself" in "I turned myself into a pickle. I'm Pickle Riiiiick"
```

# Lab 6B

Refactor your text editor or create a new Python program that allows the user to search for substrings within a file. You will need to use the PyDocs to look up additional functionality of regex. For example, **re.finditer** may help you. This refactor/program should include the functionality to:

* Return a number of how many matches were found
* Return the sentence/line in which the match was found
* Allow the user to iterate through each found instance 

**If you finish early:**

* Allow the user to replace the found instance
* Allow the user to search by line for specific line matches or lines starting with inputted substring
* Highlight/apply color to found instances



