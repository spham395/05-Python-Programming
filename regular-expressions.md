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

**Python re search and compile example:**

```py
import re

search_str = "This is a string to search"
re_search = re.compile("string")
matched_obj = re_search.search(search_str)

print matched_obj
```



