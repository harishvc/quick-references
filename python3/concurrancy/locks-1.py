#Python Locks example
#Source: http://www.python-course.eu/threads.php

import time
import threading

global special
special = 999

def change_value(i):
	global special
	special = i
	print("special=%d" %(special))

def sleeper(i,lock):
	lock.acquire()
	change_value(i)
	lock.release()
	#print("thread %d sleeps for 5 seconds" % (i))
	#time.sleep(5)
	#print("thread %d woke up" % (i))

threads = []
lock = threading.Lock() #create lock
for i in range(5):
	t = threading.Thread(target=sleeper, args=(i,lock))
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print("complete ...")


'''
special=0
special=1
special=2
special=3
special=4
complete ...
'''