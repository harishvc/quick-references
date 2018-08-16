# Python 3.5.x Quick Reference (Sort, Max, Min)

## Sort list in descending order
```python
a = [5,4,2,7,2]
a.sort(reverse=True)         #in place sort
print(a)                     #[7, 5, 4, 2, 2]
```

## Sort list of sub lists in ascending order
```python
a = [[8,9],[8,4],[6,2],[1,9]]
a.sort(reverse=False)        #in place sort
print(a)                     #[[1, 9], [6, 2], [8, 4], [8, 9]] 
```

## Sort list by length in descending order
```python
a = ["helo", "world", "!"]
a.sort(key=len,reverse=True)  #in place sort
print(a)                      #["helo", "world", "!"]
```

## Sort list of list by a specific index value
```python
#Sort by lucky #
people = [
    ['Harish', 'Chakravarthy', 22],  #first name, last name, lucky number
    ['Jon', 'Doe', 27],
    ['Foo', 'Bar', 18],
]

#sorted returns back a list and input is not modified
from operator import itemgetter
z = sorted(people,key=itemgetter(2),reverse=False)
print(z)          #[['Foo', 'Bar', 18], ['Harish', 'Chakravarthy', 22], ['Jon', 'Doe', 27]]
```

## Sort dictionary by keys
```python
>>> d= {'a':150,'z':200,'c':100}
>>> sorted(d)  #default is sort by key; output is list                        
['a', 'c', 'z']
```


## Sort dictionary by values
```python
>>> d= {'a':150,'z':200,'c':100}
>>> sorted(d,key=d.get)
['c', 'a', 'z']
```

## Find max and min key
```python
>>> d= {'a':200,'x':5,'c':3,'z':1}
>>> min(d)   #default is sort by key
'a'
>>> max(d)   #default is sort by key
'z'
```

## Find max and min value
```python
>>> d= {'c':200,'x':5,'a':3,'z':1}
>>> max(d,key=d.get)
'c'
>>> min(d,key=d.get)
'z'
```
