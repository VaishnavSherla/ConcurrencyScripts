import threading
import time

print(threading.current_thread().name, threading.active_count())


def downloadFile():
    print(f"Number of active threads: {threading.active_count()}")
    print(thread.name)
    print("Downloading file!")
    time.sleep(1)
    print("File Downloaded!")

thread = threading.Thread(target=downloadFile)
thread.start()