import threading
import time

event = threading.Event()

def downloadFile():
    print(thread.name)
    for i in range(1000):
        if not event.is_set():
            print("Downloading file chunk: ", i)
            time.sleep(1) 
    print("Download stopped!")

thread = threading.Thread(target=downloadFile)
thread.start()

time.sleep(5)
event.set()