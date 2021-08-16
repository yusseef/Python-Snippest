#Data structure linear object who follow the idea of FIFO(First in First out)
'''Queue by list'''
Queue = []
Queue.append(10)
Queue.append(20)
Queue.append(20)
Queue.pop(0) #Remove form the beginning

'''Queue by collection'''
from collections import deque
Queue = dequeu()
Queue.append(10)
Queue.append(20)
Queue.append(30)
Queue.popleft()#Remove from the beginning

'''Priority Queue'''
#We will order the queue based on the priiority which is the smallest
Queue = []
Queue.append(40)
Queue.append(30)
Queue.append(10)
Queue.append(20)
Queue.sort()#Sorted
Queue.pop()
