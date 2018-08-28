# Python 3: Concurrency Fundamentals

## Concurrency
  Concurrency is the **execution of several instruction sequences at the same time**. In an operating system, this happens when there are several process threads running in parallel.

## Critical Section
  - Critical section is a block of code that needs to be executed *atomically* - only one thread is executing the block of code at any give time
  - Here the block of code could be accessing shared resources 
  - Some *synchronization* mechanism is required at the entry and exit of the critical to prevent unexpected outcomes

## Locks
  - In Python `lock` it is currently the **lowest level synchronization primitive available**, implemented directly by the `_thread` extension module
  - A primitive `lock` has two states, `locked` or `unlocked`. It is created in the unlocked state
  - A lock is not owned by a particular thread
  - `acquire()` you can lock the critical section and then `release()` when complete
  - When `locked` all threads trying to `acquire()` wait for the state to turn to unlocked, only one thread proceeds when a `release()` call resets the state to unlocked - which one of the waiting threads proceeds is not defined, and may vary across implementations.
  - Example: multiple read and synchronous write
 
## Mutex
  - Strictly speaking, Mutex is **locking mechanism** that allows only one thread can acquire the lock - ownership associated with mutex, and only the owner can release the lock
  - A mutex can be implemented using a `lock`
  - Mutex is costly operation due to protection protocols associated with it - **priority inversion safety** and **deletion safety**

```python
#Example 1: Mutex using lock
import threading
l = threading.Lock()
try:
  l.acquire()
  print("hello world!")
  #do something
finally:
  l.release()
```

```python
#Example2: "with" to accomplish mutex using lock
import threading
import time

lock = threading.Lock()

global counter
counter = 10

class Thread(threading.Thread):
  def __init__(self, t, *args):
    threading.Thread.__init__(self, target=t, args=args)
    self.start()

def help1():
  with lock:  #acquire & release, "with" is a special keyword
    print("help1")
    print("sleeping ......")
    time.sleep(20) 
    print("awake ......")
    global counter 
    counter = counter+15
    print("help1", counter)

def help2():
  with lock:
    global counter 
    print("help2", counter)
    counter = counter-25


Thread(help1())
Thread(help2())
'''
help1
sleeping ......
awake ......
help1 25
help2 25
'''
```
## Event
  - Reference: https://graysonkoonce.com/waiting-until-a-thread-is-ready-in-python/
  - Event object is one of the simplest mechanisms for communication between threads
  - One thread signals an event and other thread waits for it
```python
#Example 3: event object
#source: https://graysonkoonce.com/waiting-until-a-thread-is-ready-in-python/
from threading import Event, Thread

class ChildProgram:
    def __init__(self, ready=None):
        self.ready = ready
        self.connection = None

    def connect(self):
        # lets make connection, expensive
        self.connection = SomeConnection()
        
        # then fire the ready event
        self.ready.set()

    def some_logic(self):
        # do something with self.connection
        pass

ready = Event()
program = ChildProgram(ready)

# configure & start thread
thread = Thread(target=program.connect)
thread.start()  #non blocking!

# block until ready
ready.wait()

# now we can safely use program
program.some_logic()
``` 

## `join`
  - Reference: https://stackoverflow.com/questions/15085348/what-is-the-use-of-join-in-python-threading
  - `join` blocks the calling thread until the thread whose join() method is called is `terminated`
  - example: `main thread`  waiting for child thread to terminate
```python
#example 4: join
def doSomething1():
  print("doSomething1 here ...")

def doSomething2():
  print("doSomething2 here ...")

t = Thread(name="childThread",target=doSomething)
print("starting child thread")
t.start()
t.join()  #main thread waiting for child thread "t" to terminate
doSomething2()

'''
starting child thread
doSomething1 here ...
doSomething2 here ...
```  

```python
#example 5: enumerate & join 
#source: http://www.bogotobogo.com/python/Multithread/python_multithreading_Enumerating_Active_threads.php

import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def f():
    r = random.randint(1,5)
    logging.debug('sleeping %s', r)
    time.sleep(r)
    logging.debug('ending')
    return

if __name__ == '__main__':
    main_thread = threading.current_thread()
    for i in range(0,3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()


    #enumerate() gathers all active threads including the calling thread     
    for t in threading.enumerate():
        if t is main_thread:
            continue
        logging.debug('joining %s', t.getName())
        t.join()
'''
(Thread-1 ) sleeping 3
(Thread-2 ) sleeping 2
(Thread-3 ) sleeping 1
(MainThread) joining Thread-1
(Thread-3 ) ending
(Thread-2 ) ending
(Thread-1 ) ending
(MainThread) joining Thread-2
(MainThread) joining Thread-3
'''
```

## Conditional Variables
  - A condition variable is always associated with a `lock`
  - `wait()` releases the lock, and then blocks until another thread awakens it by calling `notify()` or `notify_all()`. 
  - Once awakened, `wait()` re-acquires the lock and returns
  - Example: Producer consumer problem - Consumer needs to know that producer has produced! Producer needs to know there is consumer waiting!
```python
#example 6: Conditional variable implemented using lock

#original: http://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Condition_Objects_Producer_Consumer.php
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s')

def consumer(cv):
    logging.debug('Consumer thread started ...')
    with cv:
        logging.debug('Consumer waiting ...')
        cv.wait() #release the lock and block until another thread awakens
        logging.debug('Consumer consumed the resource')

def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.debug('Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll() #awake threads waiting on the lock

if __name__ == "__main__":
    condition_variable = threading.Condition()
    consumer1 = threading.Thread(name='consumer1', target=consumer, args=(condition_variable,))
    consumer2 = threading.Thread(name='consumer2', target=consumer, args=(condition_variable,))
    producer  = threading.Thread(name='producer', target=producer, args=(condition_variable,))


consumer1.start()
time.sleep(2)
consumer2.start()
time.sleep(2)
producer.start()

'''
(consumer1) Consumer thread started ...
(consumer1) Consumer waiting ...
(consumer2) Consumer thread started ...
(consumer2) Consumer waiting ...
(producer ) Producer thread started ...
(producer ) Making resource available
(producer ) Notifying to all consumers
(consumer1) Consumer consumed the resource
(consumer2) Consumer consumed the resource
'''
```

## Semaphores
  - Semaphore is **signaling mechanism** (“I am done, you can carry on” kind of signal)
  - A semaphore can allow X threads to enter (example: DB Thread pool) to enter critical section
  - A semaphore maintains a count between zero and X threads, limiting the number of threads that are simultaneously accessing a shared resource
```python
#reference: https://stackoverflow.com/questions/30032398/how-to-know-python-semaphore-value
#example 7: Semaphore
>>> from threading import Semaphore
>>> sem = Semaphore(5)
>>> sem.acquire()
True
>>> sem._value
4
>>> sem.acquire()
True
>>> sem._value
3
>>> sem.release()
>>> sem._value
4
>>> 

#example 8: Avoid deadlocks 
if(sema.acquire(blocking=False)):
    # Do something with lock taken
    sema.release()
else:
    # Do something in case when lock is taken by other
```

## Mutex vs Conditional Variable
  - Mutex and Conditional Variable are implemented using `lock`
  - Mutex is implemented using `acquire` and `release`
  - Conditional Variable is implement using `wait`, `notify` , `notifyAll`
  - Mutex don't have a notification mechanism - ideal for a sequence of operations to happen
  - Conditional variable are used for waiting for a condition to be true (state) - inbuilt notification mechanism
  - Condition variable is generally used to **avoid busy waiting** - looping repeatedly while checking a condition, wasting processor time
 
## Semaphore vs Conditional Variable
  - There is a overlap here - notification mechanism
  - Semaphore is used when you have a shared resource that can be available for X threads (X >=1)


## Mutex vs Semaphore
  - Reference: `https://www.quora.com/What-is-the-difference-between-a-mutex-and-a-semaphore`
  - Strictly speaking, Mutex is **locking mechanism** that allows only one thread can acquire the lock - ownership associated with mutex, and only the owner can release the lock
  - There is no ordering while using mutex - any of the waiting threads can acquire the lock
  - Strictly speaking, Semaphore is **signaling mechanism** than allows X threads to work in the critical section
  - Ordering can be achieved using Semephores using `notify`

## What is a deadlock? Tips to avoid deadlock
  - Reference: https://stackoverflow.com/questions/34512/what-is-a-deadlock
  - A deadlock happens when a thread is waiting for an event that **does not** occur!
  - Add timeouts to locks so the locks can be released and try again!
  - Define a lock order - obtain locks in a fixed order
  - Do not call external/third-party functions inside Critical Section without testing
  - Develop scripts that monitor thread state

## What is a Livelock?
  - Reference: https://stackoverflow.com/questions/6411803/differences-if-any-among-livelock-and-starvation-in-operating-systems
  - Much less common a problem than deadlock
  - Livelocked threads are **not blocked**  however thay are unable to make further progress - running in circles!
  - Example: Comparable to two people attempting to pass each other in a corridor: X moves to his left to let Y pass, while Y moves to his right to let X pass. Seeing that they are still 
    blocking each other, X moves to his right, while Y moves to his left - unable to make progress!

## What is Starvation?
  - Reference: https://stackoverflow.com/questions/6411803/differences-if-any-among-livelock-and-starvation-in-operating-systems
  - Much less common a problem than deadlock
  - Starvation describes a situation where a thread is unable to **gain regular access** to shared resources and is unable to make progress


## What is a race condition?
  - When multiple threads access the same resources producing **unanticiated outcomes**
  - Identify the critical section and apply *synchronization* techniques


##  Muli-threading Support & Global Interpreter Lock (GIL)
  - Cpython, Python's implementation in C enforces GIL since **memory management is not thread-safe**
  - In CPython, there are **no priorities and no thread groups**. Threads **cannot be stopped and suspended, resumed or interrupted** 
  - Thread support provided is very much basic, however a lot can still be accomplished, using the threading module.
  - In order to support multi-threaded Python programs, there's a global lock (GIL) that must be acquired by the current thread before it can safely access Python objects.
  - Thus only the thread that has acquired the GIL may operate on Python Objects or call Python C API functions.
  - The Python Interpreter keeps some book keeping info per thread, for which it uses a data structure called `PyThreadState`
  - To support multi threaded Python programs the interpreter regularly releases and reacquires the global lock, by default every **10 bytecode instructions**. This can however be changed using the `sys.setcheckinterval()`. 
  - The lock is also **released and reacquired around potentially blocking I/O operations** like reading or writing a file, so that other threads can run while the thread that requests the I/O is waiting for the I/O operation to complete
  - Long running operations such as I/O, image processing, and NumPy number crunching, happen outside the GIL.


## Concurrency vs Parallel   
  - A parallel program is one that uses a multiplicity of computational hardware (e.g. multiple processor cores) in order to perform computation more quickly. Different parts of the computation are delegated to different processors that execute at the same time (in parallel), so that results may be delivered earlier than if the computation had been performed sequentially. **Parallel programming is concerned only with efficiency**
  - Concurrency is a program-structuring technique in which there are multiple threads of control. Here threads share and modify shared resources. Concurrent program can execute on a single processor or on multiple physical processors.
  - Concurrency is hard to implement and slow since it involves Kernal transition (mutex,semaphores) and by definition block other threads.

## Additional Questions
  - [Thread and Process](https://github.com/harishvc/quick-references/blob/master/unix/intro-1.md#what-is-the-difference-between-process-and-thread)

## Examples
  - [Lock objects introduction](https://github.com/harishvc/quick-references/blob/master/python3/concurrency/locks-1.py)  
  - [Lock objects (read & write)](https://github.com/harishvc/quick-references/blob/master/python3/concurrency/locks-2.py)
  - [Conditional Variables (producer and consumer)](https://github.com/harishvc/quick-references/blob/master/python3/concurrency/conditional-variables.py)
  - [Queue object (producer and consumer)](https://github.com/harishvc/quick-references/blob/master/python3/concurrency/using-queue.py)  


## References
  - http://www.geeksforgeeks.org/mutex-vs-semaphore/
  - https://www.quora.com/What-is-the-difference-between-a-mutex-and-a-semaphore
  - http://www.geeksforgeeks.org/mutex-vs-semaphore/
  - http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/
  - http://linuxgazette.net/107/pai.html
  - http://programmers.stackexchange.com/questions/186889/why-was-python-written-with-the-gil
  - https://wiki.python.org/moin/GlobalInterpreterLock
  - http://blog.domanski.me/how-celery-fixed-pythons-gil-problem/
