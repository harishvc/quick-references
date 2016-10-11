#Implement semaphores and lock
#source: http://stackoverflow.com/questions/15651128/in-this-semaphore-example-is-it-necessary-to-lock-for-refill-and-buy


from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)
global numcandies 
numcandies = 5

def refill():
   # lock.acquire()
    try:
        candytray.release()
        global numcandies
        numcandies += 1
        print ("Refill: %d left" % numcandies) 
    except ValueError:
        pass
    #lock.release()

def buy():
    #lock.acquire()
    candytray.acquire(False)
    global numcandies
    numcandies -= 1
    print("Buy: %d left" %numcandies)
    #lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('starting at:', ctime())
    nloops = randrange(2, 6)
    print('THE CANDY MACHINE (full with %d bars)!' % MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start() # buyer
    Thread(target=producer, args=(nloops,)).start() # vendor

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
