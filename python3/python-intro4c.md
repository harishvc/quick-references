#Python3: Concurrency Fundamentals (part 1)


## Concurrency
  Concurrency is the **execution of several instruction sequences at the same time**. In an operating system, this happens when there are several process threads running in parallel.

## Critical Section
  Critical section contains shared resources and its access is protected  to prevent unexpected outcomes

## Mutex
  - Kernel resource that provide synchronization services (also called as synchronization primitives)
  - A mutex provides **mutual exclusion**. At any point of time, only **ONE** thread can work in the critical section
  - Strictly speaking, a mutex is **locking mechanism** used to synchronize access to a resource.
  - There is **ownership** associated with mutex, and only the owner can release the lock
  - Mutux can be shared across **multiple processes**
  - Mutex is costly operation due to protection protocols associated with it. Since the objective of mutex is **atomic access**.
  - Mutex also provide **priority inversion safety**. Since the mutex knows its current owner, it is possible to promote the priority of the owner whenever a higher-priority task starts waiting on the mutex.
  - Mutex provide deletion safety, where the process holding the mutex cannot be accidentally deleted. Semaphores do not provide this.

## Semaphores
  - Kernel resource that provide synchronization services (also called as synchronization primitives)
  - A semaphore is a generalized mutex
  - Semaphore is signaling mechanism (“I am done, you can carry on” kind of signal)
  - Example: listening songs on your mobile and getting a call. Here the iterrupt wakes up the call processing task
  - A semaphore has **no concept of an owner**. Any process can unlock a semaphore.
  - A semaphore can allow X threads to enter (example: DB Thread pool) and non selected threads are put to sleep
  - A semaphore maintains a count between zero and some maximum value, limiting the number of threads that are simultaneously accessing a shared resource


## Monitors
  - Wait for certain condition

## Lock & Unlock
  - Using Python `acquire()` you can lock the critical section and then `release()` when complete. 
  - Locks use `Binary Semaphore` with a default value 1. The value reduces to 0 after acquire and 1 after release.
 
## Reference
  - http://www.geeksforgeeks.org/mutex-vs-semaphore/
  - https://www.quora.com/What-is-the-difference-between-a-mutex-and-a-semaphore
  - http://www.geeksforgeeks.org/mutex-vs-semaphore/
  - http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/
 