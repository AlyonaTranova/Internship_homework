import time
from threading import Thread, BoundedSemaphore

max_dining_philosophers = 2
semaphore = BoundedSemaphore(max_dining_philosophers)

def lunch_for_philosophers(i):
    semaphore.acquire()
    try:
        print("Философ n. %i ест.\n" % i)
        time.sleep(3)
    finally:
        semaphore.release()
        print("Философ %i доел.\n" % i)
        

for i in range(5):
    th = Thread(target=lunch_for_philosophers, args=(i + 1, ))
    th.start()
