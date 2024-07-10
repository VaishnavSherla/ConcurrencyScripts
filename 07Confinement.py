# Making threads to have their own data
# Rather than having the shared data
import threading
import time

map = {}

def downloadFile(i):
    downloadedBytes = 0
    for _ in range(10):
        curr = downloadedBytes
        time.sleep(0.1)
        downloadedBytes = curr + 1
    map[i] = downloadedBytes

threads = []
for i in range(10):
    thread = threading.Thread(target=downloadFile, args=(i, ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

downloadedBytes = 0
for key in map:
    downloadedBytes += map[key]

print("Total Downloaded bytes:", downloadedBytes)
