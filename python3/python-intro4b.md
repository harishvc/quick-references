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

## Explain `zip()`
  ```zip()``` takes multiple lists and transform them into a single list of tuples
````python
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = ['a','z']
>>> d = zip (a,b,c)
>>> list(d)
[(1, 4, 'a'), (2, 5, 'z')]    #missing 3, 6!
````


## Explain *args and **kwargs  
  - * (aesteric) variable name (*foo, *bar, *args - * matters but not name) handles ALL input arguments (when #input arguments is known ahead of time), here input arguments are stored in a list
  - ** (aesteric) variable name (**foo, **bar, **args - ** matters but not name) handle ALL key value input argument
```python
#Example 1
def test1(f_arg, *foo):
    print("first normal arg:", f_arg)
    for arg in foo:
        print("another arg from *foo :", arg)
test1('hello','world','!')

output -
first normal arg: hello
another arg from *foo : world
another arg from *foo : !

#Example 2
def test2(f_arg,**bar):
    print("first normal arg:", f_arg)
    for key,value in bar.items():
        print(key, "-->", value)

a = {"key1":"hello","key2":"world","key3":"!"}
test2(1,key1="Hello",key2="World",key3="!")

output -
first normal arg: 1
key1 --> Hello
key2 --> World
key3 --> !


Reference:
1. https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
````

## Explain function decorator
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

##Explain ```dir() and help()```
  - ```help()``` provides information about a particular object directly from the interpreter
  - ```dir()``` will provide information about defined symbols - methods, errors
````python
>>> help('string')
Help on module string:

NAME
    string - A collection of string constants.

MODULE REFERENCE
    http://docs.python.org/3.4/library/string
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
...

>>>dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

>>>>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError',  
...



````

## How much space is each object taking?
  - [Measure the Real Size of Any Python Object](https://goshippo.com/blog/measure-real-size-any-python-object/)


