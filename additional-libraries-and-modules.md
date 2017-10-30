# Additional Libraries and Modules

### **A few:**

* sys, os, socket, subprocess, hashlib, shutil, math, json
* struct
* 3rd party
* Paramiko
* pip
* Hitchhikers Guide



#### Sys, OS and Subprocess

* **sys module**
  * Contains system level info
  * sys.path, sys.argv, sys.modules
* **os module**
  * interact with the os dependent functionality
  * os.path, os.walk, os.system, os.stat
* **subprocess module**
  * spawn process, stdin/stdout
  * subprocess.Popen\(\)

#### Hashlib

Hashlib implements a common interface to many different secure hash and message digest algorithms. 

```py
import hashlib

m = hashlib.md5()
m.update("password")
print m.digest()
print m.hexdigest()
```



