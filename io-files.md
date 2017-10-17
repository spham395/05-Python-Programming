# I/O: Files

Python offers a robust and insanely easy to use toolset to interact with files. 

First, a file must be opened before it can be modified... this includes creating new files. We use the **open\(\) **function to achieve this. The first argument passed is the file name; rather it exists or not. The second argument is the operation in which we would like to perform. ex read, write, overwrite, etc. 

```py
file = open("file.txt", 'r')
```

#### open\(\) Second Arguments

r  -- Opens file for read only. File pointer is placed at start of file.

rb  -- Opens a file for reading only in binary format. The file pointer is placed at the start of the file.

r+  -- Opens a file for both reading and writing. File pointer is placed at the start of the file.

rb+ -- Opens a file for both reading and writing in binary format. File pointer is placed at the start of the file.

w -- Opens a file for writing only. Overwrites the file if it exists. If the file does not exist, it creates a new one. 

wb  -- Opens a file for writing only in binary format. Overwrites the file if it exists. If it does not exist, it creates a new one. 

w+ -- Opens a file for writing and reading. Overwrites the existing file if it exists. If it does not exist, it creates a new one. 

#### 

#### 

#### File Operations

* f.write\(str\)         \# writestrto file​

* f.writelines\(str\) \# writestrto file​

* f.read\(sz\)           \# read size amount​

* f.readline\(\)         \# read next line​

* f.seek\(offset\)     \# move file pointer to offset​

* f.tell\(\)                  \# current file position​

* f.truncate\(sz\)     \# truncate the fileszbytes​

* f.close\(\)              \# close file handle​

Once the file is open, we can begin reading, adding or modifying the file's contents. 

