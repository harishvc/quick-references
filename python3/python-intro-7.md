# Python Problems

Simple problems to reinforce fundamentals

## Find quotient and remainder
```python
a = 5
b = 2
q = a//b  #2
r = a%b   #1
```

## Convert character to integer
```python
a = '1'

#Solution 1:
b = int(a)
print(b,type(b))      #1 <class 'int'>

#Solution 2:
#LIMITATION: Works for only single digits
print(a,type(a))      #1 <class 'str'>
b = ord(a) - ord('0') # subtract ascii value of '1' from ascii value of '0' , result is an integer of value 1
print(b,type(b))      #1 <class 'int'>
#
#
#Explanation
#ord('a') = 97 #ORD takes a character and returns the ascii value of the character
#ord('0') = 48    
#ord('1') = 49
#ord('2') = 50
#Subtracing ASCII value of character from the ASCII value of character 0 returns the difference - AKA result as int
```

## Convert integer to character
```python
a = chr(48)
print(a,type(a))  #0 <class 'str'>
````

## Sort list in reverse
````python
a = ["Hello","World!","Hi"]
a.sort(reverse=True)
print(a)
['World!', 'Hi', 'Hello']
```


## Sort list by length of characters
```python
a = ["Hello","World!","Hi"]
a.sort(key=len)
print(a)
['Hi', 'Hello', 'World!']
```

## Sort a string
````python
z = 'sderfga'
z2 = list(z)  #convert to list
z2.sort()     #sort list, sort() is in place , returns None
print("".join(z2))  #join converts list to string based on delimiter provided
````


## Find #rows and #cols in a matrix
````python
row = 4
col = 3
matrix=[[0 for x in range(col)] for y in range(row)]
print(matrix)
print("#rows=",len(matrix))     #4
print("#cols=",len(matrix[0]))  #3
````


## Rotate a matrix by 90 degrees clockwise
````python
#source: http://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
a = [[1,2],[3,4]]
b = list(zip(*a[::-1]))
print(b)
#[(3, 1), (4, 2)]
#Explanation:
#1. Reverse the matrix `[::-1]`
#2. Unpack the elements  `x` 
#3. `zip` each unpacked element returns a tuple
#4. Convert tuple to list
````

## Rotate a matrix by 90 degrees counter clockwise
````python
#source: http://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array?lq=1
a = [[1,2],[3,4]]
b = list(zip(*a))[::-1]
print(b)
#[(2, 4), (1, 3)]
#Explanation:
#1. zip first 
#2. rotate result
````

## Rotate a list clockwise by n positions
````python
a = [1,2,3,4,5]
n = 12
#Handle edge case where n > length of list
n = n % len(a)
print(a[-n:]+a[:-n])
#[4,5,1,2,3]
````

## Random
```python
import random
#Generate random number
print(random.random())       #0.3445306949766974              
print(random.random())       #0.1388425726388408

#Randomely pick a number from given values
a = [4,5,2,1]
print(random.choice(a))      #2
print(random.choice(a))      #1

#Shuffle given list
print(a)                     #[4,5,2,1]
random.shuffle(a)           
print(a)                     #[1, 5, 2, 4] 

#pick a value from a given range
start = 1
end = 6
random.randrange(start,end)  #1,2,3,4,5
````

