import threading
import time
 
sharedCount = 10
lock = threading.Lock()

def increment(toAdd):
    with lock:
        global sharedCount
        localCounter = sharedCount
        localCounter += toAdd
        time.sleep(1)
        sharedCount = localCounter

        print(f'{threading.current_thread().name} inc x {toAdd}, x: {sharedCount}')
    
    lock.acquire()
    # Critical section
    localCounter = sharedCount
    localCounter += toAdd
    time.sleep(1)
    sharedCount = localCounter
    print(f'{threading.current_thread().name} inc x {toAdd}, x: {sharedCount}')
    lock.release()

t1 = threading.Thread(target=increment, args=(5,))
t2 = threading.Thread(target=increment, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'The final value of x is {sharedCount}')
