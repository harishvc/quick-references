#Python Topics
List Comprehension, lambda, map, filter and generator

**List comprehension is an elegant way to define and create list in Python**

##Example 1: 
Remove vowels from a sentence
````python
input = "Hello World!"
vowels ="aeiou"
z = "".join([x for x in input if x not in vowels])
print(input)  #Hello World!
print(z)      #Hll Wrld!
````

##Example 2:
Flatten a matrix
````python
#rows & cols
from random import randint
m = 3 #row
n = 5 #col
matrix = [[ randint(1,26) for x in range(n)] for x in range(m)]
#print first and last element in the matrix
print(matrix[0][0], matrix[2][4])
#
#list of lists
matrix = [ list(range(0,5)), list(range(5,10)), list(range(10,15)) ]
print(matrix)
#[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
print([x for row in matrix for x in row ])
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
````

##Example 3:
Given two list of same length, return a dictionary with one as key and other as value
````python
country = ['India', 'Pakistan', 'Nepal', 'Bhutan', 'China', 'Bangladesh']
capital = ['New Delhi', 'Islamabad','Kathmandu', 'Thimphu', 'Beijing', 'Dhaka']
q = {y:capital[x] for x,y in enumerate(country)}
print(q)
````

###Example 4:
Given a list create a new list of squares
````python

a = [1,2,3,4,5]
print(a)   #[1,2,3,4,5]
print(list(map(lambda x: x**2,a))) #[2, 4, 6, 8, 10]
````

###Example 5:
Given a list create a new list of squares with only even numbers
````python
a = [1,2,3,4,5]
print(a)   #[1,2,3,4,5]
#1. create a new list using map
#2. pass the new list using filter and condition even number
print(list(filter(lambda x: x%2 == 0,map(lambda x: x**2,a))))
````

###Example 6:
Given a list integers create a list of characters
````python
print (list(map(chr,[65,66,67,68,69])))             
#['A', 'B', 'C', 'D', 'E']
````

**Generators are much similar to iterators except that they consume constant memory and are executed on demand 
making them a critical ingredient for optimization and in memory intense tasks
###Example 7: Print the first n event numbers **on demand**
```python
n = 10
z = (x for x in range(n) if x%2 == 0)  #() generator initialize
print(next(z))  #0
print(next(z))  #2
print(next(z))  #4
```

###Example 8: Get file contents on demand
```python
def gen():
	filename = open("12345.txt","r")
	for readline in filename:
		print("Generator invoked!")
		yield readline
	filename.close()
	print("file handle closed")

for output in gen():
	print(output)

#output
Generator invoked!
1
Generator invoked!
2
Generator invoked!
3
Generator invoked!
4
Generator invoked!
5
file handle closed
```




#References
* [Analytics Vidhya Tutorial on List Comprehension](http://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/)
