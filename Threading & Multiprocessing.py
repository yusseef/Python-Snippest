'''
            Process: An instance of a program
+takes advantage of multiple CPU
+seperate memory space
+One gil for each process
-Heaveyweight
-starting a process take more time than starting a thread

            Thread: Entity of a process, process can have multi threads
+all threads in a process share same memory
+Lightweight
+starting a thread faster than starting a process
+Great for I/O tasks

-Threading is limitied by gil obe thread at a time
-Not killable

            GIL: Global interpreter lock
-allows only one thread at a time
-Needed in CPython cause memory managmnet is not safe
Instead of GIL:
    multiprocessing
    Jython or ironPython
    python wrapper libraries

'''

from multiprocessing import Process
import os
import time
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1) 

processes = []
Num_Porcesses = os.cpu_count() #Should be the number of cpus on your machine

#Create a process

for i in range(Num_Porcesses):
    p = Process(target=square_numbers)
    processes.append(p)

#Start the processes 
for p in processes:
    p.start()

#Join the process

for p in processes:
    p.join()

print('end')