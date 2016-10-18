#Python 3.5.x  Quick Reference

## Strings
Strings are **immutable** - cannot be modified after creation
```
a = "Hello World!"
a[:5]   #'Hello'
a[:-3]  #'Hello Wor'
a[::-1] #'!dlroW olleH'  reverse string 
```

## List
Lists are mutable. Operations include `append`, `insert`, `pop`,`remove`, `del` , `sort`, `index` and split

````python
a = []
a = [1]         #1
a.append(2)     #1,2
a.pop()         #2
a.append(1)     #1,1
a.append(2)     #1,2
a.append(3)     #1,2,3
a.append(2)     #1,2,3,2
a.index(2)      #2 returns the index position of the first occurance of 2
a.remove(2)     #1,2,3  remove first occurance
a.insert(3,0)   #insert at position 3 or append 
del a           #remove a, a is not defined
del a[:]        #remove all values inside a 
del a[0:1]      #remove value at index 0
x in a          #check if x is in a, average time complexity O(n)
#LIST SPLIT
x = [1, 2, 3, 4]
print(x[3])        #4       index position 3, 4th element
print(x[-1])       #4,      last index
print(x[-3])       #2,      3rd index from the end
print(x[1:3])      #2,3     elements in index 1 & 2
print(x[:2])       #1,2     elements in index 0 & 1
print(x[1:])       #2,3,4   elements in index 1 to end of list
print(x[-2:4])     #3,2     elements between 2nd index from the end and 3rd index from end
print(x[::2])      #1,3     every other element is skipped
print(x[:-1])      #1,2,3   all values except last
print(x[-2:])      #3,4     last 2
print(x[::-1])     #4,3,2,1 reverse
```

## Tuple
Tuple are **immutable** lists. Ideal for values that don't change
````
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

len(days)  #7

for d in days:
	print(d)
````

## Set
Set is a **unordered mutable collection on unique values**. Set have **no index**. 
Set operations include `add`, `clear`, `remove`, `pop`, `discard`, `del`, `len`
````
a = set()
a.add(1)          #1
a.add(2)          #1,2
a.add(3)          #1,2,3 
a.pop()           #1 pop  random value
a.remove(3)       #2  remove a specific value
a.discard(999)    #2  remove a value that may not exist
len(a)            #1
#
a[0]
...
TypeError: 'set' object does not support indexing
#
a.clear()         #{}  remove all values
del a             #remove a, such that `a` not defined
````

## Dictionary
Dictionary is mutable and offers constant time lookup
Dictionary operations include `keys()`, `values()`, `pop`, `len`, 
````
a = {}
a[1] = 1
a[2] = 2
a[3] = 3
print(a)                        #{1: 1, 2: 2, 3: 3}
print(list(a.keys()))           #[1,2,3]  all keys
print(list(a.values()))         #[1,2,3]  all values
len(a)                          #3
a.pop(2)                        #2 return the value for key=2 , dict size reduces
if key in a.keys():             #Check if key exists
    print("key exists")
if value in a.values():          #Check if value exists
    print("value exists")
#
#
z = a.setdefault('a',1)          #1 insert key 'a' with value 1 if key 'a' does not exist and returns the value of key 'a'
z = a.setdefault('a',4)          #1 key 'a' exists, ignore new value
#
#
import collections
d = collections.defaultdict(int)  #values are of type int;handles non existant keys
d['abcd'] += 5    #5 create new key and value
d['abcd'] += 2    #7 since key exists, increment value
print(d['abcd'])  #7
````

## Queue (thread safe)
````
import queue
q = queue.Queue()
q.put(1)         #Add elements to queue
q.put(2)
print(q.get())   #1 
print(q.empty()) #Check if queue is empty
````

## DEQUE - Double ended queue, add and remove from both ends
````
import collections
dq = collections.deque()
dq.append(1)        #add on right
dq.append(2)
dq.extendleft([0])  #add elements to left
print(dq)           #deque([0, 1, 2])
print(len(dq))      #3
dq.pop()            #2
dq.popleft()        #0  
````
