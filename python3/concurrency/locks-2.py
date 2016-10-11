#Read and write using lock

#source:http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/
from urllib.request import urlopen
from threading import Thread
from threading import Lock
import time

class FetchUrls(Thread):
    def __init__(self, urls, output, lock):
        Thread.__init__(self)
        self.urls = urls
        self.output = output
        self.lock = lock
    
    def run(self):
        while self.urls:
            url = self.urls.pop()
            try:
                d = urlopen(url)
            except urlopen.URLError as e:
                print('URL %s failed: %s' % (url, e.reason))
            self.lock.acquire()
            print('lock acquired by %s' % self.name)
            self.output.write(d.read())
            print('write done by %s' % self.name)
            print('lock released by %s' % self.name)
            self.lock.release()
            print('URL %s fetched by %s' % (url, self.name))

def main():
    # list 1 of urls to fetch
    urls1 = ['http://harishvc.com']
    # list 2 of urls to fetch
    urls2 = ['http://localhost']
    lock = Lock()
    f = open('output.txt', 'wb')
    t1 = FetchUrls(urls1, f, lock)
    t2 = FetchUrls(urls2, f, lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()

if __name__ == '__main__':
    main()
 
