#Lambda annonymous function
from functools import reduce
Add_10 = lambda x: x+10 #Function to add 10 to x

Mult = lambda x,y: x*y #Function to multiple x to y

List = [(1, 2), (15, 1), (5, -1), (10, 4)]
sorted(List) #Will sort the list with x index
sorted(List, key=lambda x:x[1]) #Will sort the list with y index
sorted(List, key=lambda x:x[0] + x[1]) #Will sort the list according to sum of each

'''Map'''
List_2 = [1, 2, 3, 4, 5, 6]
List_3 = map(lambda x: x*2, List_2) #This list return a multiple of List_2

'''Filter'''
List_3 = filter(lambda x:x%2 == 0, List_2)

'''Reduce'''
Prod = reduce(lambda x,y: x*y, a)


