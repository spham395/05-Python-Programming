# UnitTesting

Unit testing is a development process where parts of small code \(called units\) are individually and independently tested for proper operation. This can of course be done manually... but it more often automated. 

Python offers a powerful built in unit testing module called unittest

**Example:**

```py
import unittest

def addx(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        # is addX(3) == 4?
        self.assertEqual(addx(3), 4)

# Run test on file launch
if __name__ == '__main__':
    unittest.main()
```

* Above, we define a function in which we want to test... a unit. 
* Then we create a test and make it a child of **TestCase**
* 


