# Numbers

### Prefixes

Prefixes convert types like **binary, hex and octal **into int.

* No prefix for decimal​

* Prefix with 0b, B for binary \(ex. 0b10 == 2\)​

* Prefix with 0x, X for hex \(ex. 0xF == 15\)​

* Prefix with 0o, O for octal \(ex. 0o100 == 64\)​

![](/assets/Screen Shot 2017-09-27 at 1.09.39 PM.png)

## Types

* int \(integer\)
  * Equivalent to C-Longs in Python 2 and non-limited in Python 3
* Long

  * Long integers of non-limited length. Exist only in Python 2

* Float \(decimal, hex, octal\)

  * Floating point numbers. Equivalent to C-Doubles

* Complex

  * Complex numbers, ex:

  ```py
  x = 1.5 + j
  y = 2
  z = x + y
  print z
  #Output: (3.5+5j)
  ```



### Numbers are IMMUTABLE!

Numbers cannot be modified in place. Be sure to either reassign your current variable or assign the number to a new variable.

![](/assets/Screen Shot 2017-09-28 at 2.00.11 PM.png)

