# Fun with Python List & String

## LIST
**Lists are mutable - values can be changed after creation**

### Reverse a list
````python
a = [1,2,3,4,5]
print(a[::-1])
[5,4,3,2,1]
````

### Reverse n elements of a list
```python
n = 3
a = [200,50,10,5,1]
b = list(reversed(a[0:n]))
print(b) #[10, 50, 200]
```

### Delete all the contents
```python
a = [1,2,3,4,5]
del a[:]
print(a) #[]
```

### Copy list
```python
a = [200, 50, 10, 5, 1]
b = a  #reference to a
a.append(0)
print(b) #[200, 50, 10, 5, 1, 0]
#
#Deep copy
a = [200, 50, 10, 5, 1]
b = a[:]
a.append(0)
print(b) #[200, 50, 10, 5, 1]
```


## STRINGS
**Strings are Immutable - Cannot change value once created**

### Trim white spaces
```python
a="   Hello   World!  "
b = a.strip() #only works on start and end!
print(b) #Hello   World!  
````
###Split a string
```python
input="Hello World!"
for x in input:
	print(x,end=",") 
#H,e,l,l,o, ,W,o,r,l,d,!,
````
###Split a split into K chunks
```python
def splitString(a,size,chunksize):
   new_input = [ a[start:start+chunksize] for start in range(0,size,chunksize)]	
   return new_input
```


