#Python Problems
Simple problems to reinforce fundamentals

##Find quotient and remainder
```python
a = 5
b = 2
q = a//b  #2
r = a%b   #1
```

##Convert character to integer
```python
a = '1'

#Solution 1:
b = int(a)
print(b,type(b))      #1 <class 'int'>

#Solution 2:
#LIMITATION: Works for only single digits
print(a,type(a))      #1 <class 'str'>
b = ord(a) - ord('0') 
print(b,type(b))      #1 <class 'int'>
#
#
#Explanation
#ord('0') = 48
#ord('1') = 49
#ord('2') = 50
#Subtracing ASCII value of character from the ASCII value of character 0 returns the difference - AKA result as int
````
##Convert integer to character
````python
a = chr(48)
print(a,type(a))  #0 <class 'str'>
````


##Sort list by length of characters
````python
a = ["Hello","World!","Hi"]
a.sort(key=len)
print(a)
['Hi', 'Hello', 'World!']
````

##Rotate a matrix by 90 degrees clockwise
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

##Rotate a matrix by 90 degrees counter clockwise
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

##Rotate a list clockwise by n positions
````python
a = [1,2,3,4,5]
n = 12
#Handle edge case where n > length of list
n = n % len(a)
print(a[-n:]+a[:-n])
#[4,5,1,2,3]
````

##Print values in a list
````python
a = [3,4,1,7]
size = 4
done = False
current = 0
while not done:
	print(a[current])
	current += 1
	#one line if statement
        #variable = value_when_true if condition else value_when_false
	done = True if current == size  else False
````
