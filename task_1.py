import time
from threading import Thread, BoundedSemaphore
import random


class DiningPhilosophers:

    def __init__(self):
        self.max_dining_philosophers = 2
        self.semaphore = BoundedSemaphore(self.max_dining_philosophers)

    def lunch_time(self, i):
        self.semaphore.acquire()
        try:
            print("Философ n. %i ест.\n" % i)
            time.sleep(random.random())
        finally:
            self.semaphore.release()
            print("Философ %i закончил есть.\n" % i)


if __name__ == '__main__':

    f = DiningPhilosophers()
    for i in range(5):
        th = Thread(target=f.lunch_time, args=(i + 1,))
        th.start()

    
