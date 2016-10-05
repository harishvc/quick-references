#Python3 Quick Reference


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
  - `yield` transfer of control is temporary and voluntary, and our function expects to regain it in the future - all the work done by the function is retained!
  - `yield` is used with generators

## What is a iterator?
  - In Python an iterator is an object which implements the iterator protocol. 
  - The iterator protocol consists of two methods. 
  - The __iter__() method, which must return the iterator object and the next() method, which returns the next element from a sequence.
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
````

## What is a generator?
  - A Generator is an iterator and implemented using one or more `yield` statements
**
````python
#generator function
def something(a):
  a = [1,2,3,4,5]
  for i in a:
    yield i

myiterator = something([1,2,3,4,5])
print(next(myiterator))  #1
print(next(myiterator))  #2
print(next(myiterator))  #3
```

##Iterator vs Generator
  - Generators & Iterators  consume **constant memory** and are **executed on demand** making them a critical ingredient for optimization and in memory intense tasks - **iterators on demand
  - Generator is a type of iterator
  - Generator is the easiest way to implement iteration on an object

## Is Python pass by value or reference or both?
 - In Python values are passed by value and reference 
 - For example numbers and strings (immutabale) passed by value
 - Lists and Disctionary are passed by value (mutable)

````python
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
````

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
````python
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
````  

## Are strings immutable? Explain
  - Yes, strings are immutable. Once created, the value cannot be modified
  - When you "change" a string, you're actually rebinding it to a newly created string object. 
  - The original object remains unchanged, even though its possible that nothing refers to it anymore
  - String concatenation is slow because concatenating strings must allocate memory for a new string and copy the contents
````python
a = "Harish"  
# 'a' is a label to the string object with value "Harish" 
a = "Ryan"    
# new string object is created and label 'a' ib pointing towards it.
# string object "Harish" continues to exit and will be cleared by the garbage collector.
````

## what is a Tuple?
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
  - Set is an **unordered collection of unique and immutable objects**
  - Set is enclosed by `{ }`
  - Sets are lists with **no duplicate entries**
  - Sets **don't support index**
  - Sets are immutable - add, remove
  - Sets are passed by reference
  - Sets don't retain order (since they don't support index)
  - Frozen set are like sets except that they are immutable
```python
a = {2,3,4}
>>> a[0] = 6  #TypeError: 'set' object does not support indexing
>>> a.pop()
2
>>> a = frozenset([1,2,3])
>>> a.add(4)
AttributeError: 'frozenset' object has no attribute 'add'
```


##References
- https://jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/
