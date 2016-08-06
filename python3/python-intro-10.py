#Python Topics

##Iterators and 2d matrix


#SPRINTF
a = "Hello %s" % ("Harish")
print(a)  #Hello Harish

#FOR LOOP
a = "Harish"
for i in a:
    print(i,end=",")  #H,a,r,i,s,h,
#
a = [11,12,13,14,15]
for i in a:
    print(i,end=",")  #11,12,13,14,15,
#
a = "Harish"
for i,v in enumerate(a):
    print(i,v)  # 0, H   1,a
#    
for i in range(5):
    print(i)         #0 1 2 3 4
#    
for i in range(0,5,2): #increment by 2
    print(i)         #0 2 4
#
for i in range(5,0,-2): #decrement by 2
    print(i)        #5,3,1

for i in range(0,5)[::-1]:
    print(i)        #4,3,2,1,0


#Initialize matrix with random values
def Initialize(matrix):
    from random import randint
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[row])):
            matrix[row][col] = randint(1,26)

#Print Matrix
def PrintMatrix(matrix): 
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[row])):
            print("%d" % (matrix[row][col]),end=" ")
        print("")
    

# Creates nxm matrix
n = 5 #rows
m = 3 #cols
matrix = [[0 for x in range(n)] for x in range(m)]

print("~~~~~~")
Initialize(matrix)
print ("%dx%d matrix >>>" % (m,n))
PrintMatrix(matrix)
    
