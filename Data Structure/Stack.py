#Stack is an array with LIFO (Last in first out)
'''Create a stack by List'''
Stack = []
Stack.append(10) #Add the value at the end of the list
Stack.append(20)
Stack.pop() #Remove the element from the end of the array

'''Create stack by collections'''
from collections import deque

stack = deque()

stack.append(10)
stack.append(20) #Add it to the end of the stack
stack.pop() #REmove from the end of the stack
