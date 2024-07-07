import threading
import time

events = {}

def downloadFile(thread_id):
    print(f"Thread {thread_id} started")
    while not events.get(thread_id, threading.Event()).is_set():
        print(f"Thread {thread_id} is doing something...")
        time.sleep(1)
    print(f"Thread {thread_id} stopped")

threads = []
for i in range(3):
    events[i] = threading.Event()
    thread = threading.Thread(target=downloadFile, args=(i,))
    threads.append(thread)
    thread.start()

time.sleep(5)

print("Interrupting Thread 1...")
events[1].set()

time.sleep(3)

for i in events:
    events[i].set()

for thread in threads:
    thread.join()

print("All threads execution completed")