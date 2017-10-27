
---

### Inheriting From a Parent Class

**Parent Class**![](/assets/Screen Shot 2017-10-27 at 1.28.06 AM.png)

**Child Class**

![](/assets/Screen Shot 2017-10-27 at 1.29.34 AM.png)

**Example Call**

```py
from USResident import USResident

 # pass init attributes. Must include additional attribute for status
resident = USResident("Joe Smo", "citizen")
resident.setAge(23) # Set age to 23

 print "{} is a {} and is {} years of age".format(resident.getLastName(), 
resident.getStatus(), resident.getAge())
```



