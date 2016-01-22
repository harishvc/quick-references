#Python Topics
List Comprehension,lambda,map and filter

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
Given a list create a new list of squares of only even numbers
````python
a = [1,2,3,4,5]
print(a)   #[1,2,3,4,5]
print(list(filter(lambda z: z is not None,map(lambda x: x**2 if (x%2==0) else None,a)))) #[4,16]
````

###Example 6:
Given a list integers create a list of characters
````python
print (list(map(chr,[65,66,67,68,69])))             
#['A', 'B', 'C', 'D', 'E']
````




#References
* [Analytics Vidhya Tutorial on List Comprehension](http://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/)
