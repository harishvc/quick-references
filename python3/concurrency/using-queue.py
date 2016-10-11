#Producer consumer problem using Queue (thread safe)

'''
task_done() indicates that a formerly enqueued task is complete. 
 - Used by queue consumer threads. 
 - For each get() used to fetch a task,  a subsequent call to task_done() 
   tells the queue that the processing on the task is complete.
'''

from threading import Thread
import time
import random
import queue

global q 
q = queue.Queue(10)

#source:http://agiliq.com/blog/2013/10/producer-consumer-problem-in-python/
class ProducerThread(Thread):
	def run(self):
		nums = range(5)
		global q
		while True:
			num = random.choice(nums)
			q.put(num)
			print("Produced", num)
			time.sleep(random.random())


class ConsumerThread(Thread):
	def run(self):
		global q
		while True:
			num = q.get()
			q.task_done() #tells the queue that the processing on the task is complete
			print("Consumed", num)
			time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()