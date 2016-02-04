#Python Problems
Simple problems to reinforce fundamentals


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


