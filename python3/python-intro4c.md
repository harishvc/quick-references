#Python3: Concurrency Fundamentals (part 1)


## Concurrency
  Concurrency is the **execution of several instruction sequences at the same time**. In an operating system, this happens when there are several process threads running in parallel.

## Critical Section
  Critical section contains shared resources and its access is protected  to prevent unexpected outcomes

## Locks
  - A primitive lock is a synchronization primitive
  - In Python, it is currently the **lowest level synchronization primitive available**, implemented directly by the _thread extension module
  - A primitive lock is in one of two states, “locked” or “unlocked”. It is created in the unlocked state
  - A lock is not owned by a particular thread
  - `acquire()` you can lock the critical section and then `release()` when complete. 
  - When more than one thread is blocked in acquire() waiting for the state to turn to unlocked, only one thread proceeds when a release() call resets the state to unlocked; which one of the waiting threads proceeds is not defined, and may vary across implementations.
  - Example: multiple read and synchronous write

## Conditional Variables
  - A condition variable is always associated with some kind of lock
  - `wait()` releases the lock, and then blocks until another thread awakens it by calling notify() or notify_all(). 
  - Once awakened, wait() re-acquires the lock and returns. 
  - Example: Producer consumer problem


## Mutex
  - Kernel resource that provide synchronization services (also called as synchronization primitives)
  - A mutex provides **mutual exclusion**. At any point of time, only **ONE** thread can work in the critical section
  - Strictly speaking, a mutex is **locking mechanism** used to synchronize access to a resource.
  - There is **ownership** associated with mutex, and only the owner can release the lock
  - Mutux can be shared across **multiple processes**
  - Mutex is costly operation due to protection protocols associated with it. Since the objective of mutex is **atomic access**.
  - Mutex also provide **priority inversion safety**. Since the mutex knows its current owner, it is possible to promote the priority of the owner whenever a higher-priority task starts waiting on the mutex.
  - Mutex provide deletion safety, where the process holding the mutex cannot be accidentally deleted. Semaphores do not provide this.

## Mutex vs Conditional Variables  
  - Mutex are designed to provide exclusive access to a shared resource - synchronized resource access. Mutexes weren't designed for use as a notification/synchronization mechanism.
  - Conditional variable is used for waiting for a condition to be true (state)
  - Mutex: Involves Kernal transition, two states - taken, free All waiters are woken up
  - Conditional Variables: Associated with mutex, ONE waiter is woken on free, Yield and re-wait on a state  

## Semaphores
  - Kernel resource that provide synchronization services (also called as synchronization primitives)
  - A semaphore is a generalized mutex
  - Semaphore is signaling mechanism (“I am done, you can carry on” kind of signal)
  - Example: listening songs on your mobile and getting a call. Here the iterrupt wakes up the call processing task
  - A semaphore has **no concept of an owner**. Any process can unlock a semaphore.
  - A semaphore can allow X threads to enter (example: DB Thread pool) and non selected threads are put to sleep
  - A semaphore maintains a count between zero and some maximum value, limiting the number of threads that are simultaneously accessing a shared resource

## Lock vs Mutex vs Semaphore
  - A lock allows only one thread to enter the part that's locked and the lock is not shared with any other processes.
  - A Mutex is the same as a lock but it can **shared by multiple processes** and results in **kernel transition**
  - A semaphore does the same as a mutex but allows X number of threads to enter the critical section and results in **kernel transition**  

## What is a deadlock? Tips to avoid deadlock.
  - All threads are waiting to acquire a lock
  - Add timeouts to locks so the locks can be released and try again!
  - Define a lock order - obtain locks in a fixed order
  - Do not call external/third-party functions inside Critical Section without testing
  - Develop scripts that monitor thread state

## What is a race condition?
  - When multiple threads access the same resources could produce unanticiated outcomes.
  - Identify the critical section and apply concurrency primitives on the critical section
  - Random sleep in on waiting threads so the kernal doesn't wake up all the waiting threads


##  Muli-threading Support & Global Interpreter Lock (GIL)
  - Cpython, Python's implementation in C enforces GIL since CPython's memory management is not thread-safe
  - In CPython threads there are no priorities and no thread groups. Threads cannot be stopped and suspended, resumed or interrupted. 
  - Thread support provided is very much basic, however a lot can still be accomplished, using the threading module.
  - In order to support multi-threaded Python programs, there's a global lock (GIL)that must be acquired by the current thread before it can safely access Python objects.
  - Thus only the thread that has acquired the GIL may operate on Python Objects or call Python C API functions.
  - The Python Interpreter keeps some book keeping info per thread, for which it uses a data structure called `PyThreadState`
  - To support multi threaded Python programs the interpreter regularly releases and reacquires the global lock, by default every **10 bytecode instructions**. This can however be changed using the `sys.setcheckinterval()`. 
  - The lock is also **released and reacquired around potentially blocking I/O operations** like reading or writing a file, so that other threads can run while the thread that requests the I/O is waiting for the I/O operation to complete
  - Potentially blocking or long-running operations, such as I/O, image processing, and NumPy number crunching, happen outside the GIL.


## Thread vs Process
  - A process is an executing instance of an application. A thread is a path of execution within a process. A process can contain many threads. 
  - Threads are easy to create, consume less resources since they share the same address space as the process creating the threads
  - Threads are used for small tasks, whereas processes are used for more ‘heavyweight’ tasks – basically the execution of applications - threads are light weight processes.
  - Threads within the same process share the same address space, whereas different processes do not. This allows threads to read from and write to the same data structures and variables, and also facilitates communication between threads. 
  - Communication between processes – also known as IPC, or inter-process communication – is quite difficult and resource-intensive
  - Processes are independent of each other.  Threads, since they share the same address space are interdependent

## Concurrency vs Parallel   
  - A parallel program is one that uses a multiplicity of computational hardware (e.g. multiple processor cores) in order to perform computation more quickly. Different parts of the computation are delegated to different processors that execute at the same time (in parallel), so that results may be delivered earlier than if the computation had been performed sequentially. **Parallel programming is concerned only with efficiency**
  - Concurrency is a program-structuring technique in which there are multiple threads of control. Here threads share and modify shared resources. Concurrent program can execute on a single processor or on multiple physical processors.
  - Concurrency is hard to implement and slow since it involves Kernal transition (mutex,semaphores) and by definition block other threads.

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
