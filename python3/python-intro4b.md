# Python 3.x: Fundamentals (part 2)

## Explain `with`
  - `with` keyword is used when working with **unmanaged resources (like file streams)**. 
  - `with` ensures that resource is "cleaned up" when the code that uses it finishes running,  
     even if exceptions are thrown.
  - **syntactic sugar** for try/except blocks.
  - **guaranteed to close the file** no matter how the nested block exits

```python
filename = "README.md"

#not using with
try:
    fp = open(filename, "r")
    for line in fp:
  print(line)
except Exception as e:
  print("oops!")
finally:
  print("done!")

#using with
with open(filename, "r") as fp:
  for line in fp:
    print(line)  #important: additional empty line!       
#no except
print("done!")
```

## Skip first line in a file
```python
with open(filename,"r") as f:
	next(f)  #iterator;skip first line
	for line in f:
	   print(line)
```

## Print Nth line
```python
with open(filename) as f:
	#readlines() returns a list with entries in each line (as values)
	print(f.readlines()[N-1])
```

## Read N bytes at a time
```python
bytes2Read = 2
with open(filename) as f:   #"Hello World!"
	#read() returns all entries as string
	z = f.read(bytes2Read)
	while z:
		print(">>", z, "<<<")  #str
		z = f.read(bytes2Read) #IMPORTANT!!!

#output
>> He <<<
>> ll <<<
>> o  <<<
>> Wo <<<
>> rl <<<
>> d! <<<
```

## Read input stream
```python
#$>cat something.txt | python a.py

import sys
try:
   for line in sys.stdin:  #input stream
     #do something
except Exception as e:
   print("oops! just handled exception")
```


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


## Explain `*args` and `**kwargs`  
  - `*` variable name (`*foo, *bar, *args - * matters but not name`) handles ALL input arguments, here input arguments are stored as **tuple**
  - `**` variable name (`**foo, **bar, **args - ** matters but not name`) handle ALL key value input argument, here input arguments are stored as **dictionary**
```python
#Example 1
def test(*ginput):
  print(type(ginput))
  print(ginput)

test(1,2,3)

<class 'tuple'>
(1, 2, 3)

#Example 2
def test(**ginput):
  print(type(ginput))
  print(ginput)

test(name="harish")

<class 'dict'>
{'name': 'harish'}


#Example 3
def test(ginputA,*ginputB,**ginputC):
  print(ginputA)
  print(ginputB)
  for key,value in ginputC.items():
        print(key, "-->", value)

test("hello world!",1,2,3,4,5,name="harish")

hello world!
(1, 2, 3, 4, 5)
name --> harish
```

## What is JSON object?
- JSON (JavaScript Object Notation) is a lightweight data-interchange format
- JSON is easy for humans to read and machines to parse
- JSON objects are surrounded by curly braces {}
- JSON objects are written in key/value pairs
- Keys must be strings, and values must be a valid JSON data type (string, number, object, array, boolean or null)
```python
example_1 = { "name":"John", "age":30, "car":null }
example_2 = {'name': 'harish', 'place': {'coordinates': [37.6624, 121.8747], 'name': 'pleasanton'}}
```


## Explain json.load(), json.loads(), json.dumps()
- json.load() read a json file
- json.loads() converts a flat object into json object. json objects
- json.dump() converts a json object to string
```python
#https://stackoverflow.com/questions/32911336/what-is-the-difference-between-json-dumps-and-json-load
#
a = {'name': 'harish', 'place': {'coordinates': [37.6624, 121.8747], 'name': 'pleasanton'}}
>>> type(a)
<class 'dict'>
#
#
>>> import json
>>> a_flat = json.dumps(a)
>>> a_flat
'{"name": "harish", "place": {"coordinates": [37.6624, 121.8747], "name": "pleasanton"}}'
>>> type(a_flat)
<class 'str'>
#
#
#
>>> b = json.loads(a_flat)
>>> b
{'name': 'harish', 'place': {'coordinates': [37.6624, 121.8747], 'name': 'pleasanton'}}
>>> type(b)
<class 'dict'>
#
#
#
>>> with open('test.json') as data_file:   
...  data = json.load(data_file)
>>> type(data)
<class 'dict'>
>>> data['menu']['value']
'File'
``` 

## Explain GIL (Global Interpreter Lock)  
  - Cpython, Python's implementation in C enforces GIL since CPython's memory management is not thread-safe. In order to support multi-threaded Python programs, there's a global lock (GIL) that must be acquired by the current thread before it can safely access Python objects. [More detailed notes on GIL](https://github.com/harishvc/quick-references/blob/master/python3/python-intro4c.md) :notes: :thumbsup:


## Explain function decorator
  - Function decorators wrap a function and modify the behaviour
  - Function decorators come in handly, when you can't modify the function (for what ever reason)
  - Example: check login before accessing page, time taken for a function to run
  - Reference:
    https://github.com/harishvc/quick-references/blob/master/python3/python-intro-9.md

## How do you process input arguments (from command line)?
```python
import sys
print("Number of arguments:", len(sys.argv))  #4
print('Argument List:', sys.argv) # ['test.py', '1', '2', '3']
print(sys.argv[2]) #2

$>python test.py 1 2 3 


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
```

## How is memory managed?
  - Memory management in Python involves a private heap containing objects and data structures
  - The management of this private heap is handled Python memory manager.
  - The Python memory manager has different components which deals with various aspects like dynamic storage, preallocation, caching, dynamic storage and garbage collection.
  - The algorithm used for garbage collecting is called Reference counting


## Python garbage collection
  - The algorithm used for garbage collecting is called **Reference counting**
  - Python keeps an internal journal of how many references refer to an object, and automatically garbage collects it when there are no more references refering to it.

## Testing
  - Unit testing - You unit test each individual piece of code (function/class)
  - Integration testing -  several individual pieces of code are tested as a group
  - Regression testing - make sure older functionality is still works with the new changes
  - Appectance testing - customer validates so that the functionality meets requirements


## Python3 default modules?
  - [Python3 default module index](https://docs.python.org/3/py-modindex.html)

## Explain ```dir() and help()```
  - ```help()``` provides information about a particular object directly from the interpreter
  - ```dir()``` will provide information about defined symbols - methods, errors
```python
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
```

## How much space is each object taking?
  - [Measure the Real Size of Any Python Object](https://goshippo.com/blog/measure-real-size-any-python-object/)


