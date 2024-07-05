import threading
import time

def downloadFile():
    print(thread.name)
    time.sleep(1)
    print("Downloading file!")

for i in range(10):
    thread = threading.Thread(target=downloadFile)
    thread.start()

for i in range(10):
    thread.join()
