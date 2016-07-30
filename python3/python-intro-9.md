#Python Topics

##Python Decorators
Decorators wrap a function and modify the behaviour

###Background
* Functions are first class object and can be passed around like variables
* When functions are passed around and latter executed, they have **access** to the environment they were **defined**

###Example 1: Determine how long it takes to run the function foo()

````python

import time
import random

def mytimer(function):
	def wrapper(*args,**kwargs):
		t1 = int(time.time() * 1000)
		freturn = function(*args,**kwargs)
		t2 = int(time.time() * 1000)
		print("time taken=", t2-t1, " ms")
		return freturn
	return wrapper

#wrap foo inside mytimer decorator    
@mytimer      
def foo(msg,sleep_time):
	print(msg, sleep_time)
	time.sleep(sleep_time) #sleep for some random time
	return len(msg) #returns back msg length

msg = "Hello"
a = [1,2,3,4,5]
for x in a:
	print(foo(msg,random.choice(a)))

output:
Hello  2
time taken= 2005  ms
6
Hello  4
time taken= 4003  ms
6
Hello  2
time taken= 2004  ms
6
Hello  2
time taken= 2005  ms
6
Hello  3
time taken= 3006  ms
6
````


#References
*[Primer on Python Decorators](https://realpython.com/blog/python/primer-on-python-decorators/)
*[Understanding Python Decorators in 12 Easy Steps!](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)   