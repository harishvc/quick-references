#Python 3.5.x Quick Reference (Sort)

## Sort list in descending order
````python
a = [5,4,2,7,2]
a.sort(reverse=True)         #in place sort
print(a)                     #[7, 5, 4, 2, 2]
````

## Sort list of sub lists in ascending order
````python
a = [[8,9],[8,4],[6,2],[1,9]]
a.sort(reverse=False)        #in place sort
print(a)                     #[[1, 9], [6, 2], [8, 4], [8, 9]] 
````

## Sort list by length in descending order
````python
a = ["helo", "world", "!"]
a.sort(key=len,reverse=True)  #in place sort
print(a)                      #["helo", "world", "!"]
````

## Sort list of list by a specific index value
```python
#Sort by lucky #
people = [
    ['Harish', 'Chakravarthy', 22],  #first name, last name, lucky number
    ['Jon', 'Doe', 27],
    ['Foo', 'Bar', 18],
]

from operator import itemgetter
z = sorted(people,key=itemgetter(2),reverse=False)
print(z)          #[['Foo', 'Bar', 18], ['Harish', 'Chakravarthy', 22], ['Jon', 'Doe', 27]]
````

## Sort dictionary by keys
```python
d= {'a':2,'x':5,'c':3}
for k in sorted(d):
	print(k, d[k])

a 2
c 3
x 5	
````


## Sort dictionary by values
```python
for k in sorted(d, key=d.get):
	print(k, d[k])

a 2
c 3
x 5
````

