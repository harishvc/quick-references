#Python Topics

##Read from file
e
#with keyword is used when working with unmanaged resources (like file streams). 
# It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown
#with open("python-intro2111.py") as f:
#        data = f.read()
        #do something with data
#        print(data)
        
xyz = "old stuff"            
def test(x):
    x[0] = 10
    print("xxxxxxxxxx")
    global xyz 
    xyz = "new stuff"
    return x
x= [5]
print(x)
print(xyz)
test(x)
print(x)  #Value changes since list is mutable - "pass by objects"
print(xyz)

