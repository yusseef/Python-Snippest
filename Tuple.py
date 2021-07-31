#Tuple : ordered, immutable, allows duplicate items
Tuple = ('banana', 25, 'HI')
Tuple_1 = 'banana', 25, 'HI' #You can declare tuple without ()

Tupple_3 = ('banana', ) # If you have one elemnt in tuple u must add , at the end

Tuple_4 = tuple(["banana", 25, True]) #You can made tuple from iterable objects like lists

item = Tuple[0] #To get specific item by index

item = Tuple[-1] #To get last item in the tuple

#Tuple_1[0] = 'MAX' # ERROR :'tuple' object does not support item assignment , Tuple can,t be edited

Tuple_5 = ('a', 'p', 'p', 'l', 'e')

len(Tuple_5) #To get the length of the tuple
Tuple_5.count('p') #To know how much that item repeated in tuple
Tuple_5.index('p') #Return the index of the first P
list(Tuple_5) #To convert tuple to a list

'''SLICING'''
Tuple_Slice = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Tuple_Slice[2:5] #From index 2 to index 5 last indec is not included
Tuple_Slice[::1] #From beginning to the end with one step
Tuple_Slice[::2] #From beginning to the end with two steps
Tuple_Slice[1:5:2] #From inde 1 to index 5 with two steps
Tuple_Slice[::-1] #REVERSE

'''Picking'''

Tuple_pick = "Max", 25, "Boston"
name, age, city = Tuple_pick # assign the value name:Max, age:25, city:Boston

import sys

list= ["Hi", 1, True]
tuple = ("Hi", 1, True)
print(sys.getsizeof(list, "Bytes")) # 120
print(sys.getsizeof(tuple, "Bytes")) # 64 Smaller cause tuple immutable