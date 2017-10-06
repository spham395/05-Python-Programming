# Mapping Types

## Dictionary

Dictionaries **are mutable **objects and consist of key-value mappings. \(ex: {key: ‘value’, key: ‘value’}  \). They are initiialized using the curly-brackets {}. Dictionaries are not ordered and support all value types.

```py
>>> my_dict = {} # create empty dictionary​
>>> my_dict['one'] = 1 # add item to the dictionary​
>>> my_dict = {'one' : 1} #create a dictionary with an item​
>>> my_dict​
{'one': 1}​
​
>>> my_dict['two'] = 2 # add item to the dictionary​
>>> my_dict​
{'one': 1, 'two': 2}​
```



### Common Dict Operations

```py
>>> d[i] = y # value of I is replaced by y​
>>> d.clear() # removes all items​
>>> d.copy() # creates a shallow copy of dict_x​
>>> d.fromkeys(S[,v]) # new dict from key, values​
>>> d.get(k[,v]) # returns dict_x[k] or v​
>>> d.items() # list of (key,value) pairs​
>>> d.iteritems() # iterator over (key,value) items​
>>> d.iterkeys() # iterator over keys of d​
>>> d.itervalues() # iterator over values of d​
>>> d.pop(k[,v]) # remove/return specified (key,value)​
>>> d.popitem() # remove/return arbitrary (key,value)​
>>> d.update(E, **F) # update d with (key,values) from E​
​
```



