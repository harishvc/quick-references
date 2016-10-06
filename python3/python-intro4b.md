#Python3: Fundamentals (part 2)

## Explain `with`
  - `with` keyword is used when working with **unmanaged resources (like file streams)**. 
  - `with` ensures that resource is "cleaned up" when the code that uses it finishes running,  
     even if exceptions are thrown.
  - **syntactic sugar** for try/finally blocks.
  - **guaranteed to close the file** no matter how the nested block exits
```python
filename = "README.md"
with open(filename, "r") as fp:
  #print(fp.read()) #print entire file
  for line in fp:
    print(line)
````

## Explain function decorators?
  - Function decorators wrap a function and modify the behaviour
  - Function decorators come in handly, when you can't modify the function (for what ever reason)
  - Example: check login before accessing page, time taken for a function to run
  - Reference:
    https://github.com/harishvc/quick-references/blob/master/python3/python-intro-9.md

## How do you process input arguments (from command line)?
````python
import sys
print("Number of arguments:", len(sys.argv))  #4
print('Argument List:', sys.argv) # ['test.py', '1', '2', '3']
print(sys.argv[2]) #2

$>python test.py 1 2 3 
````

## Python Libraries & Dependencies
```python
#Find version of libraries
pip freeze | grep selenium
selenium==2.47.3

#Get more information about the library
$>pip show selenium
Metadata-Version: 2.0
Name: selenium
Version: 2.47.3
...
````

## Testing
  - Unit testing - You unit test each individual piece of code (function/class)
  - Integration testing -  several individual pieces of code are tested as a group
  - Regression testing - make sure older functionality is still works with the new changes
  - Appectance testing - customer validates so that the functionality meets requirements


## How is memory managed?
  - Memory management in Python involves a private heap containing objects and data structures
  - The management of this private heap is handled Python memory manager.
  - The Python memory manager has different components which deals with various aspects like dynamic storage, preallocation, caching, dynamic storage and garbage collection.
  - The algorithm used for garbage collecting is called Reference counting


## Python garbage collection
  - The algorithm used for garbage collecting is called **Reference counting**
  - Python keeps an internal journal of how many references refer to an object, and automatically garbage collects it when there are no more references refering to it.


##Python3 default modules?
  - [Python3 default module index](https://docs.python.org/3/py-modindex.html)

## How much space is each object taking?
  - [Measure the Real Size of Any Python Object](https://goshippo.com/blog/measure-real-size-any-python-object/)


