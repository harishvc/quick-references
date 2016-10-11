#Producer consumer using conditional variables


'''
#source:https://docs.python.org/3.4/library/threading.html
wait() releases the lock, and then blocks until another thread awakens it by calling notify() or notify_all(). 
Once awakened, wait() re-acquires the lock and returns. It is also possible to specify a timeout.
'''

#source: http://agiliq.com/blog/2013/10/producer-consumer-problem-in-python/
from threading import Thread, Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print("Queue full, producer is waiting")
                condition.wait() #release lock, block and reaquire lock
                print("Space in queue, Consumer notified the producer")
            num = random.choice(nums)
            queue.append(num)
            print("Produced", num)
            condition.notify()  #communication
            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Nothing in queue, consumer is waiting")
                condition.wait() #release lock, block and reaquire lock
                print("Producer added something to queue and notified the consumer")
            num = queue.pop(0)
            print("Consumed", num)
            condition.notify()  #communication
            condition.release()
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()
