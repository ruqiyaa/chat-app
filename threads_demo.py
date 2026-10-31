import time
import threading

def count(name):
    for i in range(1, 4):
        print(name, i)
        time.sleep(1)

t1 = threading.Thread(target=count, args=("A",))
t2 = threading.Thread(target=count, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()
print("Done")