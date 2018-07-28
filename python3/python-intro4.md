# Python 3.x: Fundamentals (part 1)

## Table of Contents
- [Python Pros & Cons](#python-pros--cons)
- [Few difference between Python2 and Python3](#few-difference-between-python2-and-python3)
- [What is CPython?](#what-is-cpython)
- [Explain nonlocal?](#yield-vs-return)
- [What is a iterator?](#what-is-a-iterator)
- [What is a generator?](#what-is-a-generator)
- [Iterator vs Generator](#iterator-vs-generator)
- [Is Python pass by value or reference or both?](#is-python-pass-by-value-or-reference-or-both?)
- [Explain Mutable vs Immutable?](#explain-mutable-vs-immutable?)
- [Are strings immutable? Explain](#are-strings-immutable?-explain)
- [Explain Tuple](#explain-tuple)
- [What is a set? frozen set vs set?](#what-is-a-set?-frozen-set-vs-set?)
- [What is `None`?](#what-is-none?)
- [What is `''`?](#what-is-'')
- [How do you debug?](#how-do-you-debug?)
- [References](references)


## Python Pros & Cons
  - PROS
    - Python is a **dynamically typed language** 
      bind variable name to objects of different types during execution time
    - Python is **strongly typed language**
      can't concatenate string and int without converting
    - Vast inbuilt library & external libraries
    - `return` more than one value
    - Elegant code , no `;`
  - CONS
    - Indentation Horror (stick to tab or space but not both!)
    - Thread and concurrency modules are still evolving
    - Return type of function not included in function definition
    - variable type not included during declaration 
    - Global Interpreter Lock (GIL) - CPython's limitation
    - Python2 to Python3 changes


## Few difference between Python2 and Python3
  - All string are `unicode`
    _Unicode is an international encoding standard for use with different languages and scripts, by which each letter, digit, or symbol is assigned a unique numeric value_
  - `print()` is a function not a statement
  - Division of integers now returns `float` 

## What is CPython?
  CPython is the default, most widely used implementation of the Python programming language. It is written in C. CPython is a source code interpreter.


## Explain nonlocal?
  - `nonlocal` was introduced in Python3
  - `nonlocal` identifier makes a variable refer to a value in the **nearest enclosing scope excluding globals**
````python
#Example 1
global a
a = "111"
print(a)  #111
def outside():
  a = "222"  #222
  print(a)
  def inside():
    a = "333"
    print(a) #333
  inside()

#Example 2
global a
a = "111"
print(a)  #111
def outside():
  a = "222"  #222
  print(a)
  def inside():
    nonlocal a 
    a = "333"
    print(a) #333
  inside()
  print(a) #333
````

## yield vs return
  - `return` returns control to its caller, that's it. Any work done by the function and stored in local variables is lost. A new call to the function creates everything from scratch.
  - `yield` transfer of control is temporary and voluntary, and our function expects to regain it in the future - all the work done by the function is __retained!__
  - `yield` is used with generators

## What is a iterator?
  - In Python an iterator is an object which implements the iterator protocol. 
  - The iterator protocol consists of two methods. 
  - The __iter()__ method, which must return the iterator object and the __next()__ method, which returns the next element from a sequence.
  - Iterators simplify code
```python
a = "Harish"
i = iter(a)
while i:
 next(i)   #python3
 'h'
'a'
'r'
'i'
's'
'h'
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
StopIteration
```

## What is a generator?
  - A generator is an iterator but not vice versa.
  - A generator is a special kind of iterator — the elegant kind
  - A generator allows you to write your __own iterator__ in an elegant succinct syntax using `yield` (and avoid writing classes with __iter__() and __next__() methods).
  - A generator function is implemented by calling a function that has one or more yield expression
```python
# generator function
def something(a):
  for i in a:
    yield i

myiterator = something([1,2,3,4,5])
print(next(myiterator))  #1
print(next(myiterator))  #2
print(next(myiterator))  #3
```

## Iterator vs Generator
  - Generators & Iterators  consume **constant memory** and are **executed on demand** making them a critical ingredient for optimization and in memory intense tasks
  - Generator is a type of iterator
  - Generator is the easiest way to implement iteration on an object

## Is Python pass by value or reference or both?
 - In Python values are passed by value and reference 
 - For example numbers and strings (immutabale) passed by value
 - Lists and Disctionary are passed by value (mutable)

```python
#example 1: pass by value
def change(a):
  a = "hello2"

a = "hello"
change(a)
print(a)   #hello

#example 2: pass by value
a = "hello"
b = a
b = "hello2"
print(a) #hello

#example 3: pass by reference
a = list("hello")
b = a
b[4] = "2"
print(a)    #['h', 'e', 'l', 'l', '2']  , index value at position 4 changed! 

#example 4: pass by reference
def change(a2):
  a2[4] = "2"

a = list("hello")
b = a
change(b)  #value referenced by variable b is changed!
print(a) #['h', 'e', 'l', 'l', '2'] #value of variable a has changed to match b!
```

## Explain Mutable vs Immutable?
  - Mutable: Object can be modified after created. Example list, dictionary
     - Mutable are **not** thread safe
     - No need to create new objects (to handle modification)
     - When value(s) of the object changes, **all references to the object pick up the change**
  - Immutable: Object cannot be modified after creation. Example set, string
     - Thread safe
     - Simplify memory allocation
     - More secure - no buffer over flow!
     - Expensive to "change", because doing so involves creating a copy & time
```python
#string  - immutable
a = "hello"
a[0] = "H"   #TypeError: 'str' object does not support item assignment

#tuple - immutable
a = ("Harish", "Monday")
a[0] = "Ryan" #TypeError: 'tuple' object does not support item assignment

#list - mutable
a = [1,2,3]
a[0] = 0
print(a)  #0,2,3

#set - mutable
a = {1,2}
a.add(3) #continue to add values after creation
a.add(4) #continue to add values after creation
print(a) #{1,2,3,4}
```  

## Are strings immutable? Explain
  - Yes, strings are immutable. Once created, the value cannot be modified
  - When you "change" a string, you're actually rebinding it to a newly created string object. 
  - The original object remains unchanged, even though its possible that nothing refers to it anymore
  - String concatenation is slow because concatenating strings must allocate memory for a new string and copy the contents
```python
a = "Harish"  
# 'a' is a label to the string object with value "Harish" 
a = "Ryan"    
# new string object is created and label 'a' ib pointing towards it.
# string object "Harish" continues to exit and will be cleared by the garbage collector.
```

## Explain Tuple
  - A tuple is **an immutable list** enclosed in `( )`
  - Tuples are for grouping of **different types of objects** (strictly speaking) 
  - Tuples have no method
  - You can't add, remove or find values (no index) in a tuple
  - You can slice a tuple or find if a value exists
  - Tuples can be used as **keys in a dictionary**
  - Tuples are faster than lists. 
  - Ideal for **constant set of values** you'll iterate through
```python
a = (1, 2, 3)
>>> type(a)
<class 'tuple'>
>>> print(a[0:2])
(1, 2)
>>> print(True) if 2 in a else print(False)
True
>>> a[0] = 0
TypeError: 'tuple' object does not support item assignment
```

## What is a set? frozen set vs set?
  - Set is an **unordered collection of unique and mutable objects**
  - Set is enclosed by `{ }`
  - Sets are lists with **no duplicate entries and no index**
  - Sets **don't support index**
  - Sets are mutable - add, remove
  - Sets are passed by reference
  - Sets don't retain order (since they don't support index)
  - **Frozen set are like sets except that they are immutable**
```python
a = {2,3,4}
>>> a[0] = 6  #TypeError: 'set' object does not support indexing
>>> a.pop()
2
>>> a = frozenset([1,2,3])
>>> a.add(4)
AttributeError: 'frozenset' object has no attribute 'add'
```

## What is `None`?
 - python-pros--cons`None` is a special object that represents nothing but it still uses memory in Python[2] 
 - It’s a singleton, which means there is only one such object per interpreter. Example: True, False [2]
 - `None` takes us space. 16 bytes in Python 3.x

```python
>>> None = 5
File "<stdin>", line 1
SyntaxError: cannot assign to None   #special object, singleton

>>> import sys
>>> sys.getsizeof(None)
16 #bytes



>>>a 
NameError: name 'a' is not defined


>>> a = None
>>> if a:
...  print "value"    #nothing is printed
... 

>>> if not a:
...  print "empty"
... 

empty

>>> if a is None:
...  print "empty"
... 
empty
```



## What is `''`?
 - `''` is an empty string object
 - The truthiness of an empty string object `''` evaluates to `False` but probably because strings are defined as iterables and empty iterables are required to evaluate to `False` per iterator protocol[2] 
```python
>>> z = ''
>>> if z:
...  print "foo"
... else:
...  print "bar"
... 
bar

>>> sys.getsizeof('')
37
```


## How do you debug?
  - `pdb` is a command line debugger available by default
  - `pudb` is a graphical debugger that show the stack information & supports remote debugging
  - Debug information can be printed from the program
  - 
  ```python
  $>python -m pdb test.py   #you can then step, print stack etc
    help

  import pdb
  def test():
    ...
    pdb.set_trace()
    ...
    ...
  ```

## References
1. https://jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/
2. https://www.quora.com/What-is-the-difference-between-Null-and-empty-string-in-python

